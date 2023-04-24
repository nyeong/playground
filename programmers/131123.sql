select rest.food_type, rest_id, rest_name, favorites
from rest_info rest
join
  (select food_type, max(favorites) fav from rest_info group by food_type) best
  on rest.food_type = best.food_type and rest.favorites = best.fav
order by 1 desc;

-- with 절로 서브쿼리를 간략하게 표현할 수도 있음
-- with alias as (subquery)
