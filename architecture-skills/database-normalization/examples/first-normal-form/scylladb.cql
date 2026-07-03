-- Assumes a keyspace already exists and USE <keyspace>; has been run.
-- ScyllaDB uses CQL compatible with Apache Cassandra; these examples run as-is in cqlsh against ScyllaDB.

-- First Normal Form: the relational anomaly is a delimited string or numbered
-- columns standing in for an unbounded list of line items. ScyllaDB has no
-- normal forms; the equivalent decision is "one row per fact, in a query
-- table" for anything that grows without bound, versus a `set`/`list`
-- collection for a small, bounded bag of values (contrast `tags` below).
-- An unbounded list crammed into one collection column would just relocate
-- the same anomaly into a single partition.

-- Query: get all items for a given order.
CREATE TABLE order_items_by_order (
    order_id    uuid,
    product_name text,
    quantity    int,
    PRIMARY KEY ((order_id), product_name)
);

INSERT INTO order_items_by_order (order_id, product_name, quantity)
VALUES (11111111-1111-1111-1111-111111111111, 'widget', 3);
INSERT INTO order_items_by_order (order_id, product_name, quantity)
VALUES (11111111-1111-1111-1111-111111111111, 'gadget', 1);

SELECT * FROM order_items_by_order WHERE order_id = 11111111-1111-1111-1111-111111111111;

-- Contrast: a small, bounded set of full facts is fine as a collection --
-- it's never queried by individual element and can't grow past a handful.
CREATE TABLE products_catalog (
    product_id uuid PRIMARY KEY,
    product_name text,
    tags       set<text>
);

INSERT INTO products_catalog (product_id, product_name, tags)
VALUES (22222222-2222-2222-2222-222222222222, 'widget', {'clearance', 'indoor'});
