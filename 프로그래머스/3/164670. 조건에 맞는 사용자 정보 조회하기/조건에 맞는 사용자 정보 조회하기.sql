-- 코드를 입력하세요
# select *
select u.USER_ID, u.NICKNAME, concat(u.CITY," ", u.STREET_ADDRESS1, " ", u.STREET_ADDRESS2) as "전체주소",
concat(substr(u.TLNO, 1, 3), "-", substr(u.TLNO, 4, 4), "-", substr(u.TLNO, 8, 4)) as "전화번호"
# substr(u.TLNO, 1, 3)
from USED_GOODS_BOARD b
join USED_GOODS_USER u
on b.WRITER_ID = u.USER_ID
group by USER_ID, NICKNAME
having count(u.USER_ID) >= 3
order by u.USER_ID DESC;

