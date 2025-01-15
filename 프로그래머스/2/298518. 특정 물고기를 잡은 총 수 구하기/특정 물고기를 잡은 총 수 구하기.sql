select count(*) as FISH_COUNT
from FISH_INFO A
left join FISH_NAME_INFO B
on A.FISH_TYPE = B.FISH_TYPE
where B.FISH_NAME in ("BASS", "SNAPPER");