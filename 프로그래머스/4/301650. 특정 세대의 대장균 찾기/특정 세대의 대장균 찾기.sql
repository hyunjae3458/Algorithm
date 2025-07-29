select Gen3.ID
from ECOLI_DATA as Gen1
join ECOLI_DATA as Gen2 on Gen1.ID = Gen2.PARENT_ID
join ECOLI_DATA as Gen3 on Gen2.ID = Gen3.PARENT_ID
where Gen1.PARENT_ID is null
order by Gen3.ID