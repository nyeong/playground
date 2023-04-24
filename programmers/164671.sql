-- concat으로 텍스트 병합
with r as (SELECT board_id
             from USED_GOODS_BOARD
             order by views desc
             limit 1)

select concat('/home/grep/src/', board_id, '/', file_id, file_name, file_ext) as file_path
from USED_GOODS_FILE
where board_id = (select board_id from r)
order by file_id desc;
