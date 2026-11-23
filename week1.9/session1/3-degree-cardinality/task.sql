.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.

-- To see all the tables in a database
.tables

-- To see the attributes belonging to each table
.schema customers

-- And to see a count of the total number of tuples
SELECT COUNT(*) as Cardinality FROM customers; 


-- A
SELECT name, hygiene_rating FROM restaurants
WHERE hygiene_rating = 5;
-- B
SELECT name, postcode FROM restaurants
WHERE postcode LIKE 'LS6%';
-- C
SELECT name, cuisine FROM restaurants
WHERE cuisine = 'italian';
-- D
SELECT name, cuisine, hygiene_rating FROM restaurants
WHERE cuisine = 'Italian' OR
cuisine = 'Thai' AND hygiene_rating >= 0;