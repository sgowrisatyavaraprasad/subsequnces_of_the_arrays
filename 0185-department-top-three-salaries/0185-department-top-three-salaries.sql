/* Write your PL/SQL query statement below */
WITH cte AS(
    SELECT d.name AS Department , e.name AS Employee , e.salary
    FROM
    Employee e
    JOIN
    Department d
    ON e.departmentId = d.id
    ORDER BY salary DESC),
cte1 AS (
    SELECT Department , Employee , salary,
    DENSE_RANK() OVER(PARTITION BY Department ORDER BY salary DESC) AS rnk FROM cte
)
SELECT Department , Employee , salary FROM cte1
WHERE rnk <= 3;