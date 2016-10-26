-- rank in MySql using inner self join
select count(*) rank,w.name from world w join world w1 where w.population<=w1.population 
group by w.name
order by count(*)

-- median 
select * from (select count(*) rank,w.name from world w join world w1 where w.population<=w1.population 
group by w.name
order by count(*)) new_table where rank = (select floor(count(*)/2) from world);

-- running total
select count(*),sum(w1.population),w.name,w.population 
from world w join world w1 where w.population<=w1.population 
group by w.name,w.population 
order by count(*);

-- percentage of population by world sum
select name,population, population/(select sum(w.population) from world w) from world;

-- cumulative percentage
select w.name,sum(w1.population)/(select sum(w3.population) from world w3),w.population 
from world w join world w1 
where w.population <= w1.population group by w.name,w.population  order by w.population desc;
