-- Denormalization
-- Trade-off: a fully normalized schema answers "this order, its items, its
-- customer" only via a four-table join; a read-heavy dashboard pays that
-- join cost on every request. Reintroduce redundancy, deliberately, to serve it.

-- ============================================================
-- SOURCE OF TRUTH: the normalized schema from 2NF/3NF stays as-is
-- ============================================================
CREATE TABLE customers (
    customer_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    city        VARCHAR(100) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE orders (
    order_id    INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    customer_id INT UNSIGNED NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
) ENGINE=InnoDB;

CREATE TABLE products (
    product_id    INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    product_name  VARCHAR(100) NOT NULL,
    product_price DECIMAL(10,2) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE order_items (
    order_id   INT UNSIGNED NOT NULL,
    product_id INT UNSIGNED NOT NULL,
    quantity   INT UNSIGNED NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
) ENGINE=InnoDB;

-- ============================================================
-- DENORMALIZED READ TABLE: MySQL has no CREATE MATERIALIZED VIEW, so the
-- idiomatic substitute is a real table kept in sync by triggers on the
-- source tables -- an explicit, auditable sync mechanism, not a hidden one.
-- ============================================================
CREATE TABLE order_summary (
    order_id      INT UNSIGNED PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    customer_city VARCHAR(100) NOT NULL,
    item_count    INT UNSIGNED NOT NULL,
    order_total   DECIMAL(10,2) NOT NULL
) ENGINE=InnoDB;

DELIMITER $$

-- Rebuild one order's summary row whenever its line items change, instead of
-- joining four tables on every dashboard read.
CREATE TRIGGER order_items_ai AFTER INSERT ON order_items
FOR EACH ROW
BEGIN
    INSERT INTO order_summary (order_id, customer_name, customer_city, item_count, order_total)
    SELECT o.order_id, c.name, c.city,
           COUNT(*), SUM(oi.quantity * p.product_price)
    FROM orders o
    JOIN customers c ON c.customer_id = o.customer_id
    JOIN order_items oi ON oi.order_id = o.order_id
    JOIN products p ON p.product_id = oi.product_id
    WHERE o.order_id = NEW.order_id
    GROUP BY o.order_id, c.name, c.city
    ON DUPLICATE KEY UPDATE
        item_count = VALUES(item_count),
        order_total = VALUES(order_total);
END$$

DELIMITER ;

-- Consistency trade-off: order_summary is only as fresh as the last trigger
-- fire. A customer rename (UPDATE customers) needs its own trigger to fan out
-- into every summary row that copied the name, or this table drifts stale --
-- the same anomaly 3NF prevented, now reintroduced on purpose and scoped to
-- one read path.
INSERT INTO customers (customer_id, name, city) VALUES (1, 'Priya Nair', 'Austin');
INSERT INTO orders (order_id, customer_id) VALUES (1, 1);
INSERT INTO products (product_id, product_name, product_price) VALUES (101, 'Widget', 9.99);
INSERT INTO order_items (order_id, product_id, quantity) VALUES (1, 101, 2);

-- Dashboard read: one row, no join, versus the four-table join it replaces.
SELECT * FROM order_summary WHERE order_id = 1;
