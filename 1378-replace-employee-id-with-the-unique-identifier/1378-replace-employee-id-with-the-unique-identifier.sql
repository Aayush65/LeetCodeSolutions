# Write your MySQL query statement below
select s.unique_id as unique_id, f.name as name
from employees as f
left join employeeuni as s
on f.id = s.id