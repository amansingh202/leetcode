# Write your MySQL query statement below

SELECT w1.id
FROM Weather as w1
LEFT JOIN Weather as w2
ON DATE_SUB(w1.recordDate, INTERVAL 1 DAY) = w2.recordDate
WHERE w1.temperature - w2.temperature > 0;