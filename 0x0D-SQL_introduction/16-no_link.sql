-- Lists all records of the table second_table that contain a name value.
-- The results display the score and the name, in descending order.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
