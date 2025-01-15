select A.ID, count(B.ID) as CHILD_COUNT
from ECOLI_DATA A
left join ECOLI_DATA B
on A.ID = B.PARENT_ID
group by A.ID
order by A.ID;


