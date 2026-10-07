# Write your MySQL query statement below
select max(num) as num from(select num,count(*) as cnt from MyNumbers
group by num
order by count(*) asc,num desc) t
where t.cnt=1
limit 1