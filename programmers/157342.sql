-- 날짜 계산을 datediff로 해야함을 알아야함
select
  car_id,
  round(avg(datediff(end_date, start_date) + 1), 1) as average_duration
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
having average_duration > 7
order by 2 desc, 1 desc;
