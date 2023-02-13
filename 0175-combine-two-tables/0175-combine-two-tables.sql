# Write your MySQL query statement b
#select * from Address;
select firstName,lastName,City,state
from Person left join Address
on Person.personId=Address.personid;






