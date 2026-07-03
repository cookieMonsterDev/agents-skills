-- Third Normal Form (3NF)
-- Problem: customer_name/customer_city/customer_zip depend on customer_id,
-- which is itself a non-key attribute of orders -- a transitive dependency,
-- not a direct dependency on order_id.

PRAGMA foreign_keys = ON;

-- ============ BEFORE: transitive dependency through a non-key attribute ============
CREATE TABLE orders_flat (
    order_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id   INTEGER NOT NULL,
    customer_name TEXT NOT NULL,
    customer_city TEXT NOT NULL,
    customer_zip  TEXT NOT NULL
);

INSERT INTO orders_flat (customer_id, customer_name, customer_city, customer_zip) VALUES
    (501, 'Ada Lovelace', 'London', 'W1A 1AA'),
    -- Same customer, same address copied again -- depends on customer_id,
    -- not on order_id, so it is only transitively tied to this row's key.
    (501, 'Ada Lovelace', 'London', 'W1A 1AA'),
    (502, 'Grace Hopper', 'Arlington', '22201');

-- Update anomaly: Ada moving to a new city requires updating every order row
-- she has ever placed, or the rows disagree about where she lives.
-- Insertion anomaly: a new customer with no orders yet has nowhere to record
-- their name or address.
-- Deletion anomaly: deleting a customer's one and only order deletes their
-- contact information along with it.

-- ============ AFTER: split by the transitive source ============
DROP TABLE orders_flat;

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name        TEXT NOT NULL,
    city        TEXT NOT NULL,
    zip         TEXT NOT NULL
);

CREATE TABLE orders (
    order_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL REFERENCES customers (customer_id)
);

INSERT INTO customers (customer_id, name, city, zip) VALUES
    (501, 'Ada Lovelace', 'London', 'W1A 1AA'),
    (502, 'Grace Hopper', 'Arlington', '22201');

INSERT INTO orders (customer_id) VALUES
    (501),
    (501),
    (502);

-- Reconstructs the original flat view; a customer's address change is now
-- one write in `customers`, correct everywhere immediately.
SELECT o.order_id, c.customer_id, c.name, c.city, c.zip
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
ORDER BY o.order_id;
