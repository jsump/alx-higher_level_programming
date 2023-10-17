-- Display the top 3 cities' temperature during July and August ordered by desc temperature
SELECT city, AVG(value) as avg_temp FROM temperatures WHERE MONTH(month) in (7, 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
