-- 코드를 작성해주세요
select SCORE, emp.EMP_NO, EMP_NAME, POSITION, EMAIL
from HR_EMPLOYEES emp
left join (select EMP_NO, sum(SCORE) AS SCORE
from HR_GRADE
group by EMP_NO) grd
on emp.EMP_NO = grd.EMP_NO
order by SCORE DESC
limit 1;

