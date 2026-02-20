/* Write your PL/SQL query statement below */
SELECT email as Email FROM Person
HAVING COUNT(email) > 1
GROUP BY email;