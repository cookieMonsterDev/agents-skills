-- Second Normal Form (2NF)
-- Anomaly: product_name/product_price depend only on product_id, part of the
-- composite key (order_id, product_id) -- a partial dependency.

-- ============================================================
-- BEFORE: composite-keyed junction table carrying product facts
-- ============================================================
CREATE TABLE order_items (
    order_id      INT UNSIGNED NOT NULL,
    product_id    INT UNSIGNED NOT NULL,
    product_name  VARCHAR(100) NOT NULL,   -- depends only on product_id
    product_price DECIMAL(10,2) NOT NULL,  -- depends only on product_id
    quantity      INT UNSIGNED NOT NULL,
    PRIMARY KEY (order_id, product_id)
) ENGINE=InnoDB;

INSERT INTO order_items VALUES
    (1, 101, 'Widget', 9.99, 2),
    (2, 101, 'Widget', 9.99, 1);  -- product facts duplicated across orders

-- Partial dependency: product_name and product_price depend only on
-- product_id, not on the whole (order_id, product_id) key.
-- Update anomaly: repricing the Widget means updating every order line that
-- ever ordered it, or rows disagree about its current price.
-- Insertion anomaly: a new product with no orders yet has no
-- (order_id, product_id) row to attach its name/price to -- it can't be recorded.
-- Deletion anomaly: deleting the last order line for a product erases the
-- only record of its name and price.

-- ============================================================
-- AFTER: product facts split out; junction table keeps only line-specific data
-- ============================================================
DROP TABLE order_items;

CREATE TABLE products (
    product_id    INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    product_name  VARCHAR(100) NOT NULL,
    product_price DECIMAL(10,2) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE order_items (
    order_id              INT UNSIGNED NOT NULL,
    product_id            INT UNSIGNED NOT NULL,
    quantity              INT UNSIGNED NOT NULL,
    -- Not a 2NF violation: this is a deliberate historical snapshot of the
    -- price charged at purchase time, a distinct fact from the live
    -- products.product_price it happens to start out equal to.
    unit_price_at_purchase DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
) ENGINE=InnoDB;

INSERT INTO products (product_id, product_name, product_price) VALUES
    (101, 'Widget', 9.99);

INSERT INTO order_items (order_id, product_id, quantity, unit_price_at_purchase) VALUES
    (1, 101, 2, 9.99),
    (2, 101, 1, 9.99);

-- Reconstruct the "before" view via a join back to products.
SELECT oi.order_id, p.product_id, p.product_name, p.product_price,
       oi.quantity, oi.unit_price_at_purchase
FROM order_items oi
JOIN products p ON p.product_id = oi.product_id;
