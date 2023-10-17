-- List the number of records withthe same score in second table
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
