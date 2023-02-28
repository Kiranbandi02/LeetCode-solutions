# Write your MySQL query statement below
select customers.name as 'Customers' from customers
 left join 
orders
on
orders.customerId=customers.id
where orders.customerId is NULL;
