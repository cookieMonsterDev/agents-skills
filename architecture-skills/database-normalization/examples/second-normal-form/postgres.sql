-- Second Normal Form (2NF)
-- Problem: order_items is keyed by (order_id, product_id), but product_name
-- and product_price depend only on product_id, not on the whole composite
-- key -- a partial dependency.

-- ============ BEFORE: partial dependency on part of a composite key ============
CREATE TABLE order_items_flat (
    order_id      integer NOT NULL,
    product_id    integer NOT NULL,
    product_name  text NOT NULL,
    product_price numeric(10, 2) NOT NULL,
    quantity      integer NOT NULL,
    PRIMARY KEY (order_id, product_id)
);

INSERT INTO order_items_flat VALUES
    (1, 101, 'Widget', 9.99, 2),
    -- product_name/product_price for product 101 are copied again here --
    -- they depend only on product_id, not on (order_id, product_id).
    (2, 101, 'Widget', 9.99, 1),
    (1, 102, 'Gadget', 19.99, 1);

-- Update anomaly: renaming "Widget" requires updating every order line that
-- ever ordered it, or the rows disagree about the product's name.
-- Insertion anomaly: a new product with zero orders has no (order_id,
-- product_id) row to attach its name/price to, so it can't be recorded.
-- Deletion anomaly: deleting the only order line for a product deletes the
-- only place its name and price were recorded.

-- ============ AFTER: split by dependency source ============
DROP TABLE order_items_flat;

CREATE TABLE products (
    product_id    integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_name  text NOT NULL,
    product_price numeric(10, 2) NOT NULL CHECK (product_price >= 0)
);

CREATE TABLE order_items (
    order_id               integer NOT NULL,
    product_id             integer NOT NULL REFERENCES products (product_id),
    quantity               integer NOT NULL CHECK (quantity > 0),
    -- Snapshot of the price as charged at purchase time -- a distinct fact
    -- that happens to start equal to products.product_price, not a 2NF
    -- violation reintroduced by another name (see second-normal-form.md).
    unit_price_at_purchase numeric(10, 2) NOT NULL,
    PRIMARY KEY (order_id, product_id)
);

INSERT INTO products (product_id, product_name, product_price) OVERRIDING SYSTEM VALUE VALUES
    (101, 'Widget', 9.99),
    (102, 'Gadget', 19.99);

INSERT INTO order_items (order_id, product_id, quantity, unit_price_at_purchase) VALUES
    (1, 101, 2, 9.99),
    (2, 101, 1, 9.99),
    (1, 102, 1, 19.99);

-- Reconstructs the original flat view; renaming a product now touches one
-- row in `products` instead of every order line that referenced it.
SELECT oi.order_id, oi.product_id, p.product_name, p.product_price, oi.quantity
FROM order_items oi
JOIN products p ON p.product_id = oi.product_id
ORDER BY oi.order_id, oi.product_id;
