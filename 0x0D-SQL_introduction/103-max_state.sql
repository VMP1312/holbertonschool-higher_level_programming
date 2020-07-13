-- displays the max temperature of each state
SELECT state, MAX(value) AS temp_max FROM temperatures GROUP BY state ORDER BY state;