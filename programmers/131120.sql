-- MY_SQL이라 `DATE_FORMAT(field, percent-formatter)`여야함
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d')
FROM MEMBER_PROFILE
WHERE MONTH(DATE_OF_BIRTH) = 3 AND GENDER='W' AND TLNO IS NOT NULL
ORDER BY MEMBER_ID;
