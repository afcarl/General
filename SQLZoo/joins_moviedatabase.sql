-- 1. List the films where the yr is 1962 [Show id, title]
SELECT id, title
 FROM movie
 WHERE yr=1962

--2. Give year of 'Citizen Kane'.
select yr from movie where title = "Citizen Kane";

--3. List all of the Star Trek movies, include the id, title and yr (all of these movies include the words Star Trek in the title). Order results by year.
select id,title,yr from movie where instr(title,"Star Trek")

--4. What are the titles of the films with id 11768, 11955, 21191
select title from movie where id in (11768, 11955, 21191)

--5. What id number does the actress 'Glenn Close' have? 
select id from actor where name = 'Glenn Close'

--6. What is the id of the film 'Casablanca'
select id from movie where title = 'Casablanca'

--7. Obtain the cast list for 'Casablanca'.
-- what is a cast list?
-- Use movieid=11768, this is the value that you obtained in the previous question.

select name from actor where id in (select actorid from casting where movieid=(select id from movie where title = 'Casablanca'))

--8. Obtain the cast list for the film 'Alien'

select name from actor where id in (select actorid from casting where movieid=(select id from movie where title = 'Alien'))

--9. List the films in which 'Harrison Ford' has appeared
select title from movie where id in (select movieid from casting where actorid = (select id from actor where name = "Harrison Ford"))

-- 10. List the films where 'Harrison Ford' has appeared - but not in the starring role. 
--[Note: the ord field of casting gives the position of the actor. If ord=1 then this actor is in the starring role]
select title from movie where id in (select movieid from casting join actor on actor.id = casting.actorid where actor.name = "Harrison Ford" and ord!=1)

--11. List the films together with the leading star for all 1962 films.
select title, name from (movie join casting on id=movieid) join actor on actor.id = actorid where ord=1 and yr= 1962;

--12. Which were the busiest years for 'John Travolta', show the year and the number of movies he made each year for any year in which he made more than 2 movies.
SELECT yr,COUNT(title) FROM
  movie JOIN casting ON movie.id=movieid
         JOIN actor   ON actorid=actor.id
WHERE name='John Travolta'
GROUP BY yr
HAVING COUNT(title)=(SELECT MAX(c) FROM
(SELECT yr,COUNT(title) AS c FROM
   movie JOIN casting ON movie.id=movieid
         JOIN actor   ON actorid=actor.id
 WHERE name='John Travolta'
 GROUP BY yr) AS t
)

--13. List the film title and the leading actor for all of the films 'Julie Andrews' played in.
select title, name from (movie join casting on id=movieid) join actor on 
actor.id = actorid where movieid in (select movieid from casting join actor on actor.id = actorid where name = "Julie Andrews") and ord=1; 

-- 14. Obtain a list, in alphabetical order, of actors who've had at least 30 starring roles.
select name from actor where id in (select actorid from casting where ord=1
group by actorid having count(*)>=30)
order by name

--15. List the films released in the year 1978 ordered by the number of actors in the cast, then by title.
select title,count(actorid) from (movie join casting on id = movieid) join actor on actor.id  = actorid 
where yr = 1978
group by title
order by count(*) desc,title

--16. List all the people who have worked with 'Art Garfunkel'.
select distinct name from actor join casting on actor.id = actorid where movieid in
(select movieid from (movie join casting on id= movieid) join actor on actor.id = actorid where name = "Art Garfunkel") and name!='Art Garfunkel'

