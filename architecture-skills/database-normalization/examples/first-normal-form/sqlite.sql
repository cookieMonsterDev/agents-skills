-- First Normal Form (1NF)
-- Problem: `products` crams a variable-length list of items into one delimited
-- string, so no individual product is queryable, indexable, or constrained,
-- and there is no fixed answer to "how many products can an order have?"

PRAGMA foreign_keys = ON;

-- ============ BEFORE: repeating group stuffed into a delimited string ============
CREATE TABLE orders_flat (
    order_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    products      TEXT NOT NULL
);

INSERT INTO orders_flat (customer_name, products) VALUES
    ('Ada Lovelace', 'Widget,Gadget,Gizmo'),
    -- To find "every order containing a Gadget" the database must parse this
    -- string on every row; there is no way to index into one product.
    ('Grace Hopper', 'Gadget');

-- Update anomaly: adding a fourth product means rewriting the whole string;
-- deleting one product means re-splitting, editing, and re-joining the rest.
-- Insertion anomaly: recording a product for an order with no products yet
-- means inventing a placeholder string instead of just adding a row.

-- ============ AFTER: one row per product, atomic values, a real key ============
DROP TABLE orders_flat;

CREATE TABLE orders (
    order_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL
);

CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id      INTEGER NOT NULL REFERENCES orders (order_id),
    product_name  TEXT NOT NULL
);

INSERT INTO orders (order_id, customer_name) VALUES
    (1, 'Ada Lovelace'),
    (2, 'Grace Hopper');

INSERT INTO order_items (order_id, product_name) VALUES
    (1, 'Widget'),
    (1, 'Gadget'),
    (1, 'Gizmo'),
    (2, 'Gadget');

-- Reconstructs the original "order with its product list" view, but now each
-- product is its own indexable, filterable, constrainable row.
SELECT o.order_id, o.customer_name, GROUP_CONCAT(oi.product_name) AS products
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
GROUP BY o.order_id, o.customer_name
ORDER BY o.order_id;
