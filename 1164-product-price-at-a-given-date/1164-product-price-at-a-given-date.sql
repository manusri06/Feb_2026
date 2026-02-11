# Write your MySQL query statement below
select p1.product_id, ifnull(new_price,10) as price
from (select distinct product_id from Products) p1
left join Products p2
on
p1.product_id = p2.product_id and
p2.change_date = (
    select max(change_date)
    from Products 
    where product_id = p1.product_id and
    change_date <= '2019-08-16'
)