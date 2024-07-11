# Write your MySQL query statement below
SELECT id, movie, description, ROUND(rating,2) AS rating
FROM Cinema
WHERE id % 2 <> 0 AND description <> 'boring'
ORDER BY rating DESC;