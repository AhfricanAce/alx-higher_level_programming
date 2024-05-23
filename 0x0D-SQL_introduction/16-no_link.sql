--  lists all records of the table second_table of the database
-- Don’t list rows without a name
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
