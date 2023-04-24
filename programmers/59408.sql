-- mysql은 꼭 서브쿼리에 alias를 주어야 함.
select count(name)
from (select name from animal_ins group by name) a;

-- distinct 써도 됨
select count(distinct(name)) from animal_ins;
