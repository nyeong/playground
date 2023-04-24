-- 문제 이름이 문제랑 별 연관이 없네
SELECT i.animal_id, i.name
from animal_ins as i
join animal_outs as o on i.animal_id = o.animal_id
where
  i.datetime > o.datetime
order by
  i.datetime;
