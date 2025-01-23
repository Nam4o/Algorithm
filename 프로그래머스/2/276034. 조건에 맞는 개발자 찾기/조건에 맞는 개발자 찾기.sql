select distinct ID, EMAIL, FIRST_NAME, LAST_NAME
from DEVELOPERS dev
join SKILLCODES sk
on (dev.SKILL_CODE & sk.CODE) = sk.CODE and sk.NAME in ("C#", "Python")
order by dev.ID
;