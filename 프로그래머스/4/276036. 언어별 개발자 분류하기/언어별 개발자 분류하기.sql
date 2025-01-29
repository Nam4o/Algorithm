-- 코드를 작성해주세요
select 
case when group_concat(skc.CATEGORY) like ("%Front End%") and group_concat(skc.NAME) like ("%Python%") then "A"
    when group_concat(skc.NAME) like ("%C#%") then "B"
    when group_concat(skc.CATEGORY) like ("%Front End%") then "C"
    end as GRADE, dev.ID, dev.EMAIL
from DEVELOPERS dev
join SKILLCODES skc
on (dev.SKILL_CODE & skc.CODE = skc.CODE)
group by ID, EMAIL
having GRADE is not null
order by GRADE, dev.ID;

