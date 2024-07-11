# Write your MySQL query statement below

SELECT machine_id, ROUND(AVG(end_time - start_time),3) as processing_time
FROM 
(
SELECT a1.machine_id,
    MAX(CASE WHEN a1.activity_type = 'start' THEN a1.timestamp ELSE NULL END) AS start_time,
    MAX(CASE WHEN a2.activity_type = 'end' THEN a2.timestamp ELSE NULL END) AS end_time
    
    FROM Activity as a1
    JOIN Activity as a2
    ON a1.machine_id = a2.machine_id
    AND a1.process_id = a2.process_id
    GROUP BY a1.machine_id, a2.process_id
    
) AS t
GROUP BY machine_id;