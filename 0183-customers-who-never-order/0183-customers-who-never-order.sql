/* Write your PL/SQL query statement below */
SELECT c.name AS Customers FROM
Customers c
LEFT JOIN
Orders r
ON c.id = r.CUSTOMERID
WHERE r.CUSTOMERID IS NULL AND r.ID IS NULL
ORDER BY c.name;