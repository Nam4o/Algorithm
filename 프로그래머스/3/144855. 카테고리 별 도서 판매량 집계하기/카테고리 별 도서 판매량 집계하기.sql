-- 코드를 입력하세요
select b.CATEGORY, sum(s.SALES) as TOTAL_SALES

from BOOK b
join BOOK_SALES s
on b.BOOK_ID = s.BOOK_ID and s.SALES_DATE like "2022-01%"
group by b.CATEGORY
# where s.SALES_DATE like "2022-01%"
order by b.CATEGORY;
