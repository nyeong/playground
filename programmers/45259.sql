with in_duration as (
    select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where date_format(start_date, '%Y-%m') between '2022-08' and '2022-10'
    group by car_id
    having count(history_id) >= 5
)

select
  month(start_date) month, car_id, count(history_id) records
from
  CAR_RENTAL_COMPANY_RENTAL_HISTORY
where
  date_format(start_date, '%Y-%m') between '2022-08' and '2022-10'
  and car_id in (select car_id from in_duration)
group by
  month(start_date), car_id
having
  count(history_id) >= 0
order by
  1 asc, 2 desc;