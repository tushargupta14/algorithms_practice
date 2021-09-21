# Leetcode: https://leetcode.com/problems/department-top-three-salaries/
SELECT D.Name AS Department, E.Name AS Employee, E.Salary
FROM Employee AS E
LEFT JOIN Department AS D ON E.DepartmentId = D.Id
WHERE (SELECT COUNT(DISTINCT(E1.Salary)) FROM Employee AS E1 WHERE E1.DepartmentId = E.DepartmentId AND E1.Salary >= E.Salary) <= 3
