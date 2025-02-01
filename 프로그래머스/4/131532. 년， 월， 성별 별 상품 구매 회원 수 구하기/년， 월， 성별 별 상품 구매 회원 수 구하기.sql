-- 코드를 입력하세요
select YEAR(b.SALES_DATE) as YEAR,
MONTH(b.SALES_DATE) as MONTH, 
a.GENDER, count(distinct a.USER_ID) as USERS
from USER_INFO a
join ONLINE_SALE b
on a.USER_ID = b.USER_ID
where GENDER is not null
group by YEAR(b.SALES_DATE), MONTH(b.SALES_DATE), GENDER
order by YEAR, MONTH, GENDER
;