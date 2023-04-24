-- ifnull, COALESCE
-- coalesce는 표준이다. 앞에부터 차례로 검사해서 null이 아닌 빠른 값을 반환
SELECT
  ANIMAL_TYPE,
  ifnull(NAME, 'No name'),
  SEX_UPON_INTAKE
from ANIMAL_INS
order by animal_id;
