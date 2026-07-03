-- Assumes a keyspace already exists and USE <keyspace>; has been run.
-- ScyllaDB uses CQL compatible with Apache Cassandra; these examples run as-is in cqlsh against ScyllaDB.

-- Denormalization: in a relational schema this is a deliberate, named
-- exception made after normalizing. In ScyllaDB it's the default modeling
-- posture, not a special case -- tables are built per query from the start,
-- and duplicating whatever data a query needs is how a multi-entity read is
-- answered at all, since ScyllaDB has no efficient join.

-- Query: display an entire order (items, product names, customer name) from
-- a single partition read, with no join back to products or customers.
-- Both product_name (the 2NF fix) and customer_name (the 3NF fix) are
-- duplicated onto this one row on purpose. Keeping them in sync when a
-- product is renamed or a customer updates their name is the application's
-- job (write-through on update, a stream processor, or a ScyllaDB
-- materialized view with its known operational caveats) -- the redundancy
-- itself is not a bug, it's the trade this database is built around.
CREATE TABLE order_items_by_order (
    order_id      uuid,
    product_id    uuid,
    product_name  text,
    customer_name text,
    quantity      int,
    PRIMARY KEY ((order_id), product_id)
);

INSERT INTO order_items_by_order (order_id, product_id, product_name, customer_name, quantity)
VALUES (11111111-1111-1111-1111-111111111111, 22222222-2222-2222-2222-222222222222, 'widget', 'Jane Rivera', 3);
INSERT INTO order_items_by_order (order_id, product_id, product_name, customer_name, quantity)
VALUES (11111111-1111-1111-1111-111111111111, 66666666-6666-6666-6666-666666666666, 'gadget', 'Jane Rivera', 1);

SELECT * FROM order_items_by_order WHERE order_id = 11111111-1111-1111-1111-111111111111;
