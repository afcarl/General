--9. Give a distinct list of the stops which may be reached from 'Craiglockhart' by taking one bus, including 'Craiglockhart' itself, offered by the LRT company. Include the company and bus no. of the relevant services.


SELECT stopb.name,a.company, a.num
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
  JOIN stops stopa ON (a.stop=stopa.id)
  JOIN stops stopb ON (b.stop=stopb.id)
WHERE stopa.name='Craiglockhart'

--10.Find the routes involving two buses that can go from Craiglockhart to Sighthill.
-- Show the bus no. and company for the first bus, the name of the stop for the transfer,
-- and the bus no. and company for the second bus.
-- Hint
-- Self-join twice to find buses that visit Craiglockhart and Sighthill, then join those on matching stops.


select distinct X.num,X.company,X.name,Y.num,Y.company from (SELECT stopb.name,a.company, a.num
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
  JOIN stops stopa ON (a.stop=stopa.id)
  JOIN stops stopb ON (b.stop=stopb.id)
WHERE stopa.name='Craiglockhart') X

join

(SELECT stopb1.name,a1.company, a1.num
FROM route a1 JOIN route b1 ON
  (a1.company=b1.company AND a1.num=b1.num)
  JOIN stops stopa1 ON (a1.stop=stopa1.id)
  JOIN stops stopb1 ON (b1.stop=stopb1.id)
WHERE stopa1.name='Sighthill') Y
on (X.name = Y.name)
ORDER BY Cast(X.num as Integer)

