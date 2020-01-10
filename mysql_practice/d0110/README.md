# 1/10 - variable / control flow function
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
    
- ### 날짜 및 시간 함수 (date and time function)
- ### 제어 흐름 함수 (control flow function)
- ### 제어 흐름 함수 (control flow function)

