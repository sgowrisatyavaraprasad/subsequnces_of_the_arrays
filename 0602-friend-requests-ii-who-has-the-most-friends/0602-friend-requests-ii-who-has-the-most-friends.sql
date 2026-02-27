/* Write your PL/SQL query statement below */
WITH cte AS(
    SELECT requester_id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id FROM RequestAccepted
),
friends_count AS
(
    SELECT requester_id , COUNT(*) AS num FROM cte GROUP BY requester_id
)
SELECT requester_id  AS id , num
FROM friends_count WHERE num = (SELECT MAX(num) FROM friends_count);