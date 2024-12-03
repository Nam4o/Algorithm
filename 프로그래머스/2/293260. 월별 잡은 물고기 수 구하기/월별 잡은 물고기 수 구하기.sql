select COUNT(*) AS FISH_COUNT, MONTH(TIME) AS MONTH
from FISH_INFO
group by MONTH(TIME)
order by MONTH(TIME) ASC
;