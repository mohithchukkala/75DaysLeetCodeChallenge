# Write your MySQL query statement below
delete p from Person p
join Person P1 on p1.email=p.email
where p.id>P1.id;