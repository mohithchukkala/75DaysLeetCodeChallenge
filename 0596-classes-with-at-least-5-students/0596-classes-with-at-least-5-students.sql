# Write your MySQL query statement below
select class from (select class,count(*) as counting from Courses
                    group by class
                    order by counting desc) t
where t.counting>=5;