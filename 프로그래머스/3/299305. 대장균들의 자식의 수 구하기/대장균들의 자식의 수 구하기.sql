select P.ID, COUNT(C.ID) as CHILD_COUNT
from ECOLI_DATA as C
right join ECOLI_DATA as P on C.PARENT_ID = P.ID
group by P.ID;
