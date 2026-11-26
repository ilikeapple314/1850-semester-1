.headers on
.mode column

-- add tasks below
-- sqlite3 database_file.db to open the database
-- .read sql_file.sql to run the queries

BEGIN;
INSERT INTO orders
(order_id, customer_id, restaurant_id)
VALUES (5003, 12, 3);
INSERT INTO order_items
VALUES (5003, 87, 2);
COMMIT; -- or ROLLBACK;