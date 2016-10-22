-- 1.The example shows the number who responded for:
-- question 1
-- at 'Edinburgh Napier University'
-- studying '(8) Computer Science'
-- Show the the percentage who STRONGLY AGREE

SELECT A_STRONGLY_AGREE
  FROM nss
 WHERE question='Q01'
   AND institution='Edinburgh Napier University'
   AND subject='(8) Computer Science'

-- 2. Show the institution and subject where the score is at least 100 for question 15.
select institution, subject from nss
where score >= 100 and question = "Q15";

-- Show the institution and score where the score for '(8) Computer Science' is less than 50 for question 'Q15'

SELECT institution,score
  FROM nss
 WHERE question='Q15'
   AND score<50
   AND subject='(8) Computer Science'

-- Show the subject and total number of students who responded to question 22 for each of the subjects '(8) Computer Science' and '(H) Creative Arts and Design'.

select subject, sum(response)
from nss
where subject in ('(8) Computer Science','(H) Creative Arts and Design') and question = "Q22"
group by subject


-- Show the subject and total number of students who A_STRONGLY_AGREE to question 22 for each of the subjects '(8) Computer Science' and '(H) Creative Arts and Design'.
-- HINT
-- The A_STRONGLY_AGREE column is a percentage. To work out the total number of students who strongly agree 
--you must multiply this percentage by the number who responded (response) and divide by 100 - take the SUM of that.

select subject, sum(response*A_STRONGLY_AGREE/100)
from nss
where subject in ('(8) Computer Science','(H) Creative Arts and Design') and question = "Q22"
group by subject

--6. Show the percentage of students who A_STRONGLY_AGREE to question 22 for the subject '(8) Computer Science' show the same figure for the subject '(H) Creative Arts and Design'.
--Use the ROUND function to show the percentage without decimal places.

select subject, round(sum(response*A_STRONGLY_AGREE)/sum(response),0)
from nss
where subject in ('(8) Computer Science','(H) Creative Arts and Design') and question = "Q22"
group by subject

--7. Show the average scores for question 'Q22' for each institution that include 'Manchester' in the name.
-- The column score is a percentage - you must use the method outlined above to multiply the percentage by the response 
-- and divide by the total response. Give your answer rounded to the nearest whole number.

SELECT institution,round(sum(response*score)/sum(response),0)
  FROM nss
 WHERE question='Q22'
   AND (institution LIKE '%Manchester%')
group by institution
ORDER BY institution

-- 8. Show the institution, the total sample size and the number of computing students for institutions in Manchester for 'Q01'.
SELECT institution,sum(sample),sum(
case 
when subject = "(8) Computer Science" then sample*1
else 0
end
) 
  FROM nss
 WHERE question='Q01'
   AND (institution LIKE '%Manchester%')
group by institution