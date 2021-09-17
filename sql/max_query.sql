/* Leetcode: https://leetcode.com/problems/department-highest-salary/*/

Select Department.Name Department, emp1.Name Employee, emp1.Salary Salary from
Employee emp1 join Department on emp1.DepartmentId = Department.Id
where emp1.Salary = (Select Max(Salary) from Employee emp2 where emp2.DepartmentId = emp1.DepartmentId);