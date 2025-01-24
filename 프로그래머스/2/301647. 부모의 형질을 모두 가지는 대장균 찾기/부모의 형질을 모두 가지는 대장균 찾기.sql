select c.ID, c.GENOTYPE, p.GENOTYPE as PARENT_GENOTYPE
# select *
from ECOLI_DATA as c
join ECOLI_DATA as p
on (c.GENOTYPE & p.GENOTYPE) = p.GENOTYPE and c.PARENT_ID = p.ID
order by c.ID asc;