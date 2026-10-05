# Write your MySQL query statement below
select customer_number from (select customer_number,count(*) as counting  from Orders
group by customer_number
order by counting desc) t
limit 1;