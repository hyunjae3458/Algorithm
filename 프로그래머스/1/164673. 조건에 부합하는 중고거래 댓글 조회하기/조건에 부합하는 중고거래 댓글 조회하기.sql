select B.TITLE, B.BOARD_ID, R.REPLY_ID, R.WRITER_ID, R.CONTENTS, date_format(R.CREATED_DATE,"%Y-%m-%d") as CREATED_DATE
from USED_GOODS_BOARD as B 
join USED_GOODS_REPLY as R on B.BOARD_ID = R.BOARD_ID 
where date_format(B.CREATED_DATE,"%Y-%m") = "2022-10"
order by R.CREATED_DATE asc, B.TITLE asc