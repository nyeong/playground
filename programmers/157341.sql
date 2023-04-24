-- group by로 유일하게 하거나
-- distinct 쓰거나
-- 아니면 car_id가 CAR_RENTAL_COMPANY_CAT 테이블의 pk일테니 여기서 유일함을
-- 이용하거나
with oct as (select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY
               where month(start_date) = 10
               group by car_id)

select oct.car_id
from oct
left outer join CAR_RENTAL_COMPANY_CAR car on oct.car_id = car.car_id
where car.car_type = '세단'
order by oct.car_id desc;

SELECT DISTINCT CAR_ID 
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = '세단' 
AND CAR_ID IN(SELECT CAR_ID
              FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
              WHERE MONTH(START_DATE) = 10)
ORDER BY CAR_ID DESC;
