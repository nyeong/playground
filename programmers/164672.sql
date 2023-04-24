-- case .. when을 활용하여 분류
select
  board_id, writer_id, title, price,
  CASE
    WHEN status = 'SALE' THEN '판매중'
    WHEN status = 'RESERVED' THEN '예약중'
    WHEN status = 'DONE' THEN '거래완료'
    ELSE '알 수 없는 상태'
  END AS status
from USED_GOODS_BOARD
where
  created_date = '2022-10-05'
order by
  board_id desc;
