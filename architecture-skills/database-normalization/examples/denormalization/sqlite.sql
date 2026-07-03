-- Denormalization
-- Starting point: a fully normalized schema (orders/customers/products/
-- order_items) that answers "this order's items, with product names and the
-- customer's name" only by joining four tables. At scale, or on a read-heavy
-- dashboard, that join cost -- not any remaining anomaly -- becomes the
-- bottleneck.

PRAGMA foreign_keys = ON;

-- ============ Source of truth: fully normalized schema (2NF/3NF result) ============
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    city        TEXT NOT NULL
);

CREATE TABLE products (
    product_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name  TEXT NOT NULL,
    product_price REAL NOT NULL CHECK (product_price >= 0)
);

CREATE TABLE orders (
    order_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL REFERENCES customers (customer_id)
);

CREATE TABLE order_items (
    order_id               INTEGER NOT NULL REFERENCES orders (order_id),
    product_id             INTEGER NOT NULL REFERENCES products (product_id),
    quantity               INTEGER NOT NULL CHECK (quantity > 0),
    unit_price_at_purchase REAL NOT NULL,
    PRIMARY KEY (order_id, product_id)
);

INSERT INTO customers (name, city) VALUES
    ('Ada Lovelace', 'London'),
    ('Grace Hopper', 'Arlington');

INSERT INTO products (product_name, product_price) VALUES
    ('Widget', 9.99),
    ('Gadget', 19.99);

INSERT INTO orders (customer_id) VALUES (1), (2);

INSERT INTO order_items (order_id, product_id, quantity, unit_price_at_purchase) VALUES
    (1, 1, 2, 9.99),
    (1, 2, 1, 19.99),
    (2, 1, 1, 9.99);

-- ============ Denormalized copy: a summary table for the read-heavy path ============
-- SQLite has no materialized view; a real table is the idiomatic substitute.
-- The base tables stay normalized; this table is the named, scoped exception
-- that trades write-time consistency for read-time speed on a dashboard
-- query that would otherwise pay a four-table join on every request.
CREATE TABLE order_summary (
    order_id               INTEGER NOT NULL,
    customer_name          TEXT NOT NULL,
    customer_city          TEXT NOT NULL,
    product_name           TEXT NOT NULL,
    quantity               INTEGER NOT NULL,
    unit_price_at_purchase REAL NOT NULL,
    line_total             REAL NOT NULL,
    PRIMARY KEY (order_id, product_name)
);

-- Initial population (in production: triggers on source tables or a scheduled job).
INSERT INTO order_summary
SELECT
    o.order_id,
    c.name,
    c.city,
    p.product_name,
    oi.quantity,
    oi.unit_price_at_purchase,
    (oi.quantity * oi.unit_price_at_purchase)
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
JOIN order_items oi ON oi.order_id = o.order_id
JOIN products p ON p.product_id = oi.product_id;

-- Read-heavy dashboard query: one flat scan, no runtime join.
SELECT * FROM order_summary ORDER BY order_id;

-- The summary table is a snapshot, not a live read of the base tables: a new
-- order, or a customer's city change, will not appear here until the table
-- is rebuilt or kept in sync by triggers/application code. Pick a refresh
-- cadence that matches how much staleness this read path can tolerate.
