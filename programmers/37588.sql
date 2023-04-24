-- cast(datetime as date) 한 후 left로 잘라서 출력하는 법도 있는듯?
-- 좋은 방법은 아닌듯
select animal_id, name, date_format(datetime, '%Y-%m-%d')
from ANIMAL_INS;
