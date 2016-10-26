-- rank in MySql using inner self join
select count(*) rank,w.name from world w join world w1 where w.population<=w1.population 
group by w.name
order by count(*)

-- median 
select * from (select count(*) rank,w.name from world w join world w1 where w.population<=w1.population 
group by w.name
order by count(*)) new_table where rank = (select floor(count(*)/2) from world); 