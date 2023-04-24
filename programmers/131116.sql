-- 풀이가 많아서 어떤 풀이가 좋은지 잘 모르겠음
select f.category, price, product_name
from food_product f
join (select category, max(price) as max_price from food_product group by category) m
  on max_price = f.price and f.category = m.category
where f.category in ('과자', '국', '김치', '식용유')
order by price desc;

SELECT CATEGORY, PRICE MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE PRICE IN
    (
    SELECT MAX(PRICE) MAX_PRICE
    FROM FOOD_PRODUCT
    GROUP BY CATEGORY
    )
AND CATEGORY IN ('과자', '국', '김치', '식용유')
ORDER BY 2 DESC;

