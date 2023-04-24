-- like의 % 사용법
select animal_id, name
from ANIMAL_INS
where
  name like '%el%'
  and animal_type = 'Dog'
order by name;
