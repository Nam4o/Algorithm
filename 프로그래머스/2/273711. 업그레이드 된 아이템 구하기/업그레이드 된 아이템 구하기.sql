# -- 코드를 작성해주세요
# # select *
# select base.ITEM_ID, base.ITEM_NAME, base.RARITY, sub.PARENT_ITEM_ID
# from ITEM_INFO as base
# join (select info.ITEM_ID, info.ITEM_NAME, info.RARITY, tree.PARENT_ITEM_ID

# from ITEM_INFO as info
# left join ITEM_TREE as tree
# on info.ITEM_ID = tree.ITEM_ID
#       # and tree.PARENT_ITEM_ID is not null
# # where info.RARITY = "RARE"
#      ) as sub
# on base.ITEM_ID = sub.ITEM_ID
# where sub.PARENT_ITEM_ID = (select ITEM_ID
#                              # from ITEM_INFO as a
#                              # join ITEM_TREE as b
#                              # on a.ITEM_ID = b.ITEM_ID
#                              # where b.RARITY = "RARE"
#                              from ITEM_INFO
#                              where RARITY = "RARE";
#                              )
#                              ;


# # select info.ITEM_ID, info.ITEM_NAME, info.RARITY, tree.PARENT_ITEM_ID

# # from ITEM_INFO as info
# # left join ITEM_TREE as tree
# # on info.ITEM_ID = tree.ITEM_ID
# # where info.RARITY = "RARE"
# # ;

select base.ITEM_ID, base.ITEM_NAME, base.RARITY
from ITEM_INFO as base
where base.ITEM_ID in (select tree.ITEM_ID
                       from ITEM_TREE as tree
                       where tree.PARENT_ITEM_ID in (select sub.ITEM_ID
                                                     from ITEM_INFO as sub
                                                     where sub.RARITY = "RARE"))
order by 1 desc;
                                                     