# Leetcode : https://leetcode.com/problems/nth-highest-salary/
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M = N-1;
  IF (SELECT DISTINCT(COUNT(*)) FROM Employee) < N THEN
        RETURN NULL;
  END IF;
  RETURN (
      # Write your MySQL query statement below
        SELECT DISTINCT(Salary) FROM Employee ORDER BY Salary DESC LIMIT M, 1
  );
END