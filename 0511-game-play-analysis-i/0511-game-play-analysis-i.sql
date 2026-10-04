# Write your MySQL query statement below
select player_id,event_date as first_login from(
    select *,dense_rank() over(partition by player_id order by event_date) as logins from Activity
) t
where t.logins=1;