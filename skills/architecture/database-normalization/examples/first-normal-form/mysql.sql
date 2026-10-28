-- First Normal Form (1NF)
-- Anomaly: a comma-delimited string standing in for a repeating list of order
-- line items, so individual products can't be indexed, filtered, or joined on.

-- ============================================================
-- BEFORE: products crammed into one delimited VARCHAR column
-- ============================================================
CREATE TABLE orders (
    order_id      INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    products      VARCHAR(255) NOT NULL  -- 1NF violation: not atomic, a hidden list
) ENGINE=InnoDB;

INSERT INTO orders (customer_name, products) VALUES
    ('Alice Chen', 'Widget,Gadget,Gizmo'),  -- three facts hiding in one cell
    ('Bob Duarte', 'Widget');

-- MySQL has JSON columns but no native array type, and MySQL enforces neither
-- form of this violation -- a comma string or a JSON array both slip in silently.
-- Update anomaly: renaming "Widget" to "Widget Pro" means parsing and rewriting
-- every `products` string that contains it, in application code, or rows drift.
-- Insertion anomaly: recording a fourth product on Alice's order means
-- string-editing the existing cell instead of adding a row.
-- Deletion anomaly: removing one product from the middle of the list requires
-- rebuilding the whole string; there's no row to just delete.

-- ============================================================
-- AFTER: one row per product, in its own child table
-- ============================================================
DROP TABLE orders;

CREATE TABLE orders (
    order_id      INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE order_items (
    order_id     INT UNSIGNED NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (order_id, product_name),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
) ENGINE=InnoDB;

INSERT INTO orders (customer_name) VALUES ('Alice Chen'), ('Bob Duarte');

INSERT INTO order_items (order_id, product_name) VALUES
    (1, 'Widget'), (1, 'Gadget'), (1, 'Gizmo'),
    (2, 'Widget');

-- Reconstruct the "before" view: one row per order, products aggregated back
-- into a list only at read time, on demand, not stored that way.
SELECT o.order_id, o.customer_name,
       GROUP_CONCAT(oi.product_name ORDER BY oi.product_name SEPARATOR ',') AS products
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
GROUP BY o.order_id, o.customer_name;
