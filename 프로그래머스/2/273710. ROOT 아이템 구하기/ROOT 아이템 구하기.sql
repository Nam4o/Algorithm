-- 코드를 작성해주세요
select info.ITEM_ID, info.ITEM_NAME
# select *
from ITEM_INFO info
left join ITEM_TREE tree
on info.ITEM_ID = tree.ITEM_ID
where tree.PARENT_ITEM_ID is null
order by info.ITEM_ID ASC;
# where;