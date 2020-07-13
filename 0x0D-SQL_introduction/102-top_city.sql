-- Displays the top 3 of cities temperature during July and August ordered by temperature
SELECT city, AVG(value) as temp_avg FROM temperatures WHERE month >= 7 AND month <= 8 GROUP BY city ORDER BY temp_avg DESC LIMIT 3;
