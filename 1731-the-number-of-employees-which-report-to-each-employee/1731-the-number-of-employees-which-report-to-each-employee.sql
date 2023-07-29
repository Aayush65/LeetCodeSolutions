# Write your MySQL query statement below

select e2.employee_id as employee_id, e2.name as name, count(e1.age) as reports_count, round(avg(e1.age), 0) as average_age
from employees e1
inner join employees e2
on e1.reports_to = e2.employee_id
where e1.reports_to is not null
group by e1.reports_to
order by employee_id