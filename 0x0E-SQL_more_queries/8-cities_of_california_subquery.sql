-- Lists all the cities of California that can be found in the database hbtn_0d_usa.
-- Second line
SELECT id, name
FROM cities
WHERE state_id = 1 GROUP BY id ASC;
