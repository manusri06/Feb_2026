# Write your MySQL query statement below
select person_name
from (
    select person_name,
    sum(weight) over (order by turn) as total_w
    from Queue
)t
where total_w <= 1000
order by total_w DESC
LIMIT 1
