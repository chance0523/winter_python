# 1/10 - [variable](#variable) / [built-in functions](#control flow function) / [join](#JOIN) / union
- ### variable
  - #### create variable
    + ##### SET @variable_name;
      ```mysql
      SET @a = 1;
      SET @b = 'MySQL';
      ```
   - #### variable type conversion
     + ##### CAST ( ... AS variable type)
        ```mysql
        -- 실수 => 정수
        SELECT
            CAST(AVG(amount) AS SIGNED INTEGER) AS '평균 구매 갯수'
        FROM buyTbl;
        ```
     + ##### CONVERT ( ... , variable type)
       ```mysql
       -- 숫자가 포함된 문자열
       SELECT CONVERT('2nd', SIGNED INTEGER); -- 2
       SELECT CONVERT('2nd123', SIGNED INTEGER); -- 2
       ```
***
- ### 제어 흐름 함수 (control flow function)
   - #### IF / IFNULL / NULLIF
     + ##### IF(수식, True 값1, False 값2)
       ```mysql
       SELECT IF(100 < 200, '크다', '작다'); -- 크다
       SELECT IF(100 > 200, '크다', '작다'); -- 작다
       ```
     + ##### IFNULL(수식1, 수식2) : 수식1이 NULL이 아니면 수식1 반환, NULL 이면 수식2 반환
       ```mysql
       SELECT IFNULL(NULL, 'NULL값이다'); -- NULL값이다
       SELECT IFNULL(100 + 300, 'NULL값이다.'); -- 400
       ```
     + ##### NULLIF(수식1, 수식2) : 수식1과 수식2가 같으면 NULL, 다르면 수식1 반환
       ```mysql
       SELECT NULLIF(50 + 50, 40 + 60); -- NULL
       SELECT NULLIF(50 + 50, 40 + 40); -- 100
       ```
   - #### CASE    
     + ##### CASE 값1 WHEN 값2 THEN 결과값1 ... ELSE 결과값2 END
       ```mysql
       SET @age = 5;
       SELECT 
          CASE @age
              WHEN 0 THEN '영'
              WHEN 5 THEN '오'
              WHEN 10 THEN '십'
              ELSE '지정된 숫자가 아니다'
          END AS '결과';
       ```
- ### 문자열 함수 (string function)
   - #### CONCAT / CONCAT_WS
     + ##### CONCAT(문자열1, 문자열2, ... ) : 문자열이나 레코드를 이어준다.
       ```mysql
       SELECT 
           CONCAT('가수이름 => ', name) AS '이름',
           CONCAT(height, 'cm') AS '키'
       FROM
           userTbl;
       
       /* 이름                     키
          가수이름 => 바비킴	    176cm */
       ```
     + ##### CONCAT_WS(구분자, 문자열1, 문자열2, ...) : 문자열이나 레코드를 구분자와 함께 이어준다.
       ```mysql
       SELECT 
           CONCAT_WS('/',
                '방탄소년단',
                '블랙핑크',
                '레드벨벳') AS '아이돌 그룹';
       -- 방탄소년단/블랙핑크/레드벨벳
       ```
   - #### FORMAT
     + ##### FORMAT(숫자/필드명/수식, 소숫점 자리수) : 소숫점 자리 표시
       ```MySQL
       SET @myNumber = 123.567890;
       SELECT FORMAT(@myNumber, 1); -- 123.6
       SELECT FORMAT(@myNumber, 4); -- 123.5679
       ```
   - #### INSERT / REPLACE
     + ##### INSERT(문자열, 시작위치, 길이, 교체문자열) : 특정 글자로 교체
       ```MYSQL
       SET @userPhone = "010-5555-6606";
       SELECT INSERT(@userPhone, 5, 4, "####"); -- 010-####-6606
       SELECT INSERT(@userPhone, 10, 4, "####"); -- 010-5555-####
       SELECT INSERT(INSERT(@userPhone, 10, 4, '####'), 5, 4, "####"); -- 010-####-####
       ``` 
     + ##### REPLACE(문자열, 원래문자열, 교체문자열) : 특정 글자로 교체
       ```MYSQL
       SELECT REPLACE(@userPhone, "5555", "####"); -- 010-####-6606
       ```
   - #### LEFT / RIGHT / SUBSTRING
     + ##### LEFT(문자열, 길이) / RIGHT(문자열, 길이) : 왼쪽이나 오른쪽을 기준으로 길이만큼 잘라서 표시 
       ```MYSQL
       SELECT @userPhone, LEFT(@userPhone, 3);  -- 010-5555-6606	010
       SELECT @userPhone, RIGHT(@userPhone, 3); -- 010-5555-6606	606
       ```
     + ##### SUBSTRING(문자열, 시작위치, 길이) : 시작위치에서 길이만큼 잘라서 표시  
       ```MYSQL
       SELECT SUBSTRING(@userPhone, 5, 9); -- 5555-6606
       ```
   - #### REPEAT / LPAD / RPAD
     + ##### REPEAT(문자열, 반복횟수) : 문자열을 횟수만큼 반복한다.
       ```MYSQL
       SET @userName = "신짱구";
       SELECT REPEAT(@userName, 3); -- 신짱구신짱구신짱구
       ```
     + ##### LPAD(문자열, 길이, 채울 문자열), RPAD(문자열, 길이, 채울문자열) : 왼쪽이나 오른쪽에 길이만큼 늘려 문자열을 채운다.
       ```MYSQL
       SELECT LPAD(@userName, 10, " * "), RPAD(@userName, 20, " * ");
       --  *  *  신짱구	|신짱구 *  *  *  *  *  *
       ```
   - #### LTRIM / RTRIM / TRIM
     + ##### LTRIM(문자열), RTRIM(문자열), TRIM(문자열) : 문자열 공백 없애기
       ```MYSQL
       SET @userM = "       근 하 신 년       ";
       SELECT CONCAT('###',LTRIM(@userM), '###'); -- ###근 하 신 년       ###
       SELECT CONCAT('###',RTRIM(@userM), '###'); -- ###       근 하 신 년###
       SELECT CONCAT('###',TRIM(@userM), '###');  -- ###근 하 신 년###
       ```
       
- ### 날짜 및 시간 함수 (date and time function)
   - #### variable type : YEAR / DATE / TIME / DATETIME
     + ##### 
       ```mysql
       SELECT CAST('2019-12-25 12:12:12' AS DATETIME); -- 2019-12-25 12:12:12
       SELECT CAST('2020-12-12 12:12:12' AS DATE) AS DATE; -- 2020-12-12
       SELECT CAST('2019-12-25 12:12:12' AS TIME) AS TIME; -- 12:12:12
       ```
   - #### NOW / SYSDATE / CURDATE / CURTIME
     + ##### NOW() / SYSDATE() : 현재의 날짜와 시간 표시
       ```MYSQL
       SELECT 
           NOW(),
           CAST(NOW() AS DATE) AS '현재 날짜',
           CAST(NOW() AS TIME) AS '현재 시각';
       -- 2020-01-10 12:30:25	2020-01-10	12:30:25
       ```
     + ##### CURDATE() : 현재 날짜 표시 / CURTIME() : 현재 시각 표시
       ```MYSQL
       SELECT 
           SYSDATE(),
           CURDATE() AS '현재 날짜',
           CURTIME() AS '현재 시각';
       -- 2020-01-10 12:31:10	2020-01-10	12:31:10
       ```
   - #### YEAR / MONTH / DAY / HOUR / MINUTE / SECOND
     + ##### 날짜 또는 시간에서 연, 월, 일, 시, 분, 초를 구한다.
       ```MYSQL
       SELECT 
	       YEAR(NOW()) AS 'YEAR',
	       MONTH(NOW()) AS 'MONTH',
	       DAY(NOW()) AS 'DAY',
           HOUR(NOW()) AS 'HOUR',
           MINUTE(NOW()) AS 'MINUTE',
           SECOND(NOW()) AS 'SECOND';
       ```
   - #### DAYOFWEEK / MONTHNAME / DAYOFYEAR
     + ##### DAYOFWEEK(날짜) : 요일표시 1 ~ 7 (일 ~ 토)
     + ##### MONTHNAME(날짜) : 달을 영문으로 표시
     + ##### DAYOFYEAR(날짜) : 1년 중 몇번째 날인지 표시
       ```MySQL
       SET @today = DAYOFWEEK(NOW());
       SELECT 
           CASE @today
               WHEN 1 THEN '일요일'
               WHEN 2 THEN '월요일'
               WHEN 3 THEN '화요일'
               WHEN 4 THEN '수요일'
               WHEN 5 THEN '목요일'
               WHEN 6 THEN '금요일'
               ELSE '토요일'
           END AS '오늘 요일';
       ```
   - #### DATEDIFF / TIMEDIFF
     + ##### DATEDIFF(날짜1, 날짜2) : 날짜1 - 날짜2 / TIMEDIFF(시간1, 시간2) : 시간1 - 시간2
       ```MYSQL
       SELECT DATEDIFF('2021-01-01',NOW());  -- 357
       SELECT TIMEDIFF('17:50:00', CURTIME());  -- 03:51:20
       ```
     
- ### 시스템 함수 (system function)
   - #### DATABASE / USER / VERSION
     + ##### DATABASE : 사용중인 데이터베이스 표시 / USER : 사용자 표시 / VERSION : MySQL 버전 표시
       ```mysql
       SELECT 
           DATABASE() AS '데이터베이스',
           USER() AS '사용자',
           VERSION() AS 'MySQL 버전';
       -- world	root@localhost	8.0.18
       ```
***
- ### JOIN
   - #### INNER JOIN / OUTER JOIN / CROSS JOIN / SELF JOIN
     + ##### INNER JOIN
       ```MYSQL
       SELECT 
           B.userID AS '아이디',
           B.prodName AS '상품명',
           B.amount AS '수량',
           U.name AS '이름',
           U.addr AS '지역'
       FROM
           buyTbl B
               INNER JOIN
           userTbl U ON B.userID = U.userID;
       -- 아이디   상품명  수량  이름    지역
       --  KBS    운동화   2   김범수   경남
       ```
     + ##### OUTER JOIN
       ```MYSQL
       SELECT 
           S.stdName, S.addr, C.clubName, C.roomNo
       FROM
           stdTbl S
               LEFT OUTER JOIN
           stdclubTbl SC ON S.stdName = SC.stdName
               LEFT OUTER JOIN
           clubTbl C ON SC.clubName = C.clubName
       ORDER BY S.stdName;
       -- stdName addr clubName roomNo
       --  김범수  경남   바둑    102호
       ```
     + ##### CROSS JOIN
     + ##### SELF JOIN
     
- ### UNION / UNION ALL / NOT IN / IN
   - #### UNION / UNION ALL
     + ##### UNION
     + ##### UNION ALL
   - #### NOT IN / IN
     + ##### NOT IN
     + ##### IN
