-- Assumes a keyspace already exists and USE <keyspace>; has been run.

-- Second Normal Form: the relational anomaly is a non-key column that
-- depends on only part of a composite key. Cassandra has no composite-key
-- partial dependency to violate -- the analogous decision is which columns
-- to duplicate into a per-query table so a SELECT never has to look back at
-- another table for a name that's needed on every row.

-- Query: look up a single product by id.
CREATE TABLE products (
    product_id    uuid PRIMARY KEY,
    product_name  text,
    product_price decimal
);

INSERT INTO products (product_id, product_name, product_price)
VALUES (22222222-2222-2222-2222-222222222222, 'widget', 9.99);

SELECT * FROM products WHERE product_id = 22222222-2222-2222-2222-222222222222;

-- Query: get all line items for an order.
-- product_name is duplicated in on purpose so this read never joins back to
-- products; keeping it in sync after a rename is the application's job.
-- unit_price_at_purchase is NOT a copy of the live price -- it's a
-- historical snapshot of what was actually charged, a distinct fact that
-- happens to start out equal to product_price.
CREATE TABLE order_items_by_order (
    order_id               uuid,
    product_id             uuid,
    product_name           text,
    quantity               int,
    unit_price_at_purchase decimal,
    PRIMARY KEY ((order_id), product_id)
);

INSERT INTO order_items_by_order (order_id, product_id, product_name, quantity, unit_price_at_purchase)
VALUES (11111111-1111-1111-1111-111111111111, 22222222-2222-2222-2222-222222222222, 'widget', 3, 9.99);

SELECT * FROM order_items_by_order WHERE order_id = 11111111-1111-1111-1111-111111111111;
