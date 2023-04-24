-- 문제가 헷갈리게 되어 있는데... 게시글의 작성일로 정렬해야함
select
  TITLE, b.BOARD_ID, REPLY_ID, r.WRITER_ID, r.CONTENTS,
  date_format(r.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
from USED_GOODS_REPLY as r
left outer join USED_GOODS_BOARD as b on b.BOARD_ID = r.BOARD_ID
where date_format(b.CREATED_DATE, '%Y-%m') = '2022-10'
order by r.CREATED_DATE ASC, TITLE ASC;