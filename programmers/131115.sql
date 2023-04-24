SELECT *
FROM food_product
order by price desc
limit 1;

-- 혹은 서브쿼리로 해결

SELECT *
FROM food_product
WHERE price = (select max(price) from food_product);
