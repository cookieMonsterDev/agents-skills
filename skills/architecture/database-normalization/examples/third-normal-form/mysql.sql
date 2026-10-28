-- Third Normal Form (3NF)
-- Anomaly: customer_name/customer_city/customer_zip depend on customer_id,
-- itself a non-key attribute of orders -- a transitive dependency.

-- ============================================================
-- BEFORE: customer facts riding along on the orders table
-- ============================================================
CREATE TABLE orders (
    order_id      INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    customer_id   INT UNSIGNED NOT NULL,
    customer_name VARCHAR(100) NOT NULL,  -- depends on customer_id, not order_id
    customer_city VARCHAR(100) NOT NULL,  -- depends on customer_id, not order_id
    customer_zip  VARCHAR(10)  NOT NULL   -- depends on customer_id, not order_id
) ENGINE=InnoDB;

INSERT INTO orders (customer_id, customer_name, customer_city, customer_zip) VALUES
    (501, 'Priya Nair', 'Austin', '78701'),
    (501, 'Priya Nair', 'Austin', '78701');  -- same customer, copied on every order

-- Transitive dependency: order_id -> customer_id -> {customer_name, city, zip}.
-- Update anomaly: Priya moving to Dallas means updating every order row she's
-- ever placed, or the rows disagree about where she lives.
-- Insertion anomaly: a new customer with no orders yet has nowhere to record
-- their name or address.
-- Deletion anomaly: deleting a customer's only order deletes their contact
-- information along with it.

-- ============================================================
-- AFTER: customer facts split into their own table, referenced by foreign key
-- ============================================================
DROP TABLE orders;

CREATE TABLE customers (
    customer_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    city        VARCHAR(100) NOT NULL,
    zip         VARCHAR(10)  NOT NULL
) ENGINE=InnoDB;

CREATE TABLE orders (
    order_id    INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    customer_id INT UNSIGNED NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
) ENGINE=InnoDB;

INSERT INTO customers (customer_id, name, city, zip) VALUES
    (501, 'Priya Nair', 'Austin', '78701');

INSERT INTO orders (customer_id) VALUES (501), (501);

-- Reconstruct the "before" view via a join; a customer's address now lives
-- (and is updated) in exactly one place.
SELECT o.order_id, c.customer_id, c.name AS customer_name,
       c.city AS customer_city, c.zip AS customer_zip
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id;
