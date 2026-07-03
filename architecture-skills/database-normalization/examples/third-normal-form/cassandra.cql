-- Assumes a keyspace already exists and USE <keyspace>; has been run.

-- Third Normal Form: the relational anomaly is a non-key column that
-- depends on another non-key column (customer_name depending on
-- customer_id) rather than on the row's own key. A Cassandra SELECT can't
-- join orders back to customers, so any table built to show an order with
-- the customer's name has to carry that name on the row itself.

-- Query: look up a customer by id.
CREATE TABLE customers (
    customer_id uuid PRIMARY KEY,
    name        text,
    city        text,
    zip         text
);

INSERT INTO customers (customer_id, name, city, zip)
VALUES (33333333-3333-3333-3333-333333333333, 'Jane Rivera', 'Austin', '78701');

SELECT * FROM customers WHERE customer_id = 33333333-3333-3333-3333-333333333333;

-- Query: list a customer's orders.
-- customer_name is duplicated in so this single-partition read never looks
-- up customers separately. Renaming a customer means writing to both
-- customers and every orders_by_customer row for them (or accepting
-- staleness until a fan-out job catches up).
CREATE TABLE orders_by_customer (
    customer_id   uuid,
    order_id      uuid,
    customer_name text,
    PRIMARY KEY ((customer_id), order_id)
);

INSERT INTO orders_by_customer (customer_id, order_id, customer_name)
VALUES (33333333-3333-3333-3333-333333333333, 11111111-1111-1111-1111-111111111111, 'Jane Rivera');

SELECT * FROM orders_by_customer WHERE customer_id = 33333333-3333-3333-3333-333333333333;
