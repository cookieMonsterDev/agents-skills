-- Denormalization
-- Starting point: a fully normalized schema (orders/customers/products/
-- order_items) that answers "this order's items, with product names and the
-- customer's name" only by joining four tables. At scale, or on a read-heavy
-- dashboard, that join cost -- not any remaining anomaly -- becomes the
-- bottleneck.

-- ============ Source of truth: fully normalized schema (2NF/3NF result) ============
CREATE TABLE customers (
    customer_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name        text NOT NULL,
    city        text NOT NULL
);

CREATE TABLE products (
    product_id    integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_name  text NOT NULL,
    product_price numeric(10, 2) NOT NULL CHECK (product_price >= 0)
);

CREATE TABLE orders (
    order_id    integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id integer NOT NULL REFERENCES customers (customer_id)
);

CREATE TABLE order_items (
    order_id               integer NOT NULL REFERENCES orders (order_id),
    product_id             integer NOT NULL REFERENCES products (product_id),
    quantity               integer NOT NULL CHECK (quantity > 0),
    unit_price_at_purchase numeric(10, 2) NOT NULL,
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

-- ============ Denormalized copy: a materialized view for the read-heavy path ============
-- The base tables stay normalized; this view is the named, scoped exception
-- that trades write-time consistency for read-time speed on a dashboard
-- query that would otherwise pay a four-table join on every request.
CREATE MATERIALIZED VIEW order_summary AS
SELECT
    o.order_id,
    c.name        AS customer_name,
    c.city        AS customer_city,
    p.product_name,
    oi.quantity,
    oi.unit_price_at_purchase,
    (oi.quantity * oi.unit_price_at_purchase) AS line_total
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
JOIN order_items oi ON oi.order_id = o.order_id
JOIN products p ON p.product_id = oi.product_id;

CREATE UNIQUE INDEX order_summary_order_product_idx
    ON order_summary (order_id, product_name);

-- Read-heavy dashboard query: one flat scan, no runtime join.
SELECT * FROM order_summary ORDER BY order_id;

-- The view is a snapshot, not a live read of the base tables: a new order,
-- or a customer's city change, will not appear here until refreshed.
-- `REFRESH MATERIALIZED VIEW order_summary` rebuilds it but blocks
-- concurrent reads of the view for its duration; `REFRESH MATERIALIZED VIEW
-- CONCURRENTLY order_summary` (requires the unique index above) keeps it
-- readable during the rebuild at the cost of a slower refresh. Either way,
-- the view is stale between refreshes -- pick a refresh cadence (a
-- scheduled job, a trigger-driven `pg_cron` run, or after each batch of
-- writes) that matches how much staleness this read path can tolerate.
