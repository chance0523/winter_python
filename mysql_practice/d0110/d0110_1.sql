USE sqldb;
-- 변수 생성과 출력 p.234
-- SET @변수명 = 초기값; -- 변수의 선언 및 값 대입
-- SELECT @변수명 -- 변수의 값 출력

SET @a = 1;
SET @b = 10;
SET @c = 'MySQL';
SET @d = 'sqLite';

SELECT @a, @b, @c, @d;
SELECT @a, @b, @a + @b, @a * @b;
SELECT @c, @d, @c + @d; -- 'MySQL', 'sqLite', '0'

-- 테이블과 변수 함께 사용하기
SELECT * FROM userTbl;

SET @deco = '***';
SELECT @deco;
SELECT 
    userID AS '아이디', @deco AS ' ', addr AS '지역'
FROM
    userTbl;
    
-- userTbl에서 키가 180이 넘는 레코드만 추출한 후 아래와 같은 형태로 출력하여라
SET @irm = '가수이름 =>';
SET @cm = 'cm';
SELECT @irm;
SELECT 
    @irm AS ' ', name AS '이름', height AS '키', @cm AS ' '
FROM
    userTbl
WHERE
    height > 180;

-- 데이터 형변환 CASTING p.236
-- CAST ( ... AS 데이터형식)
-- CONVERT ( ... , 데이터형식)
-- 데이터형식 : BINARY, CHAR(), DATE, TIME, SIGNED INTERGER, UNSIGNED INTEGER

-- 평균 구매 개수가 실수 => 정수
SELECT * FROM buyTbl;
-- 실수형으로 결과값 리턴
SELECT AVG(amount) AS '평균 구매 개수' FROM buyTbl; -- 3.3571
-- 양의 정수형으로 결과값 리턴
SELECT 
    CAST(AVG(amount) AS SIGNED INTEGER) AS '평균 구매 개수'
FROM
    buyTbl; -- 3

SELECT CAST(23.5 AS CHAR(10));
-- 숫자가 포함된 문자열 => 양의 정수
SELECT CAST('2nd' AS SIGNED INTEGER); -- 2
SELECT CONVERT('2nd' ,SIGNED INTEGER); -- 2
SELECT CAST('2nd123' AS SIGNED INTEGER); -- 2
SELECT CAST('-5' as SIGNED INTEGER); -- -5

/* ------------------------------------------ */
-- 제어흐름함수 p.239
-- IF(수식, True값1, False값2)
-- IFNULL(수식1, 수식2)
-- : 수식1이 NULL이 아니면 수식1 반환, NULL 이면 수식2 반환
-- NULLIF(수식1, 수식2)
-- : 수식1과 수식2가 같으면 NULL, 다르면 수식1 반환

SELECT IF(100 < 200, '크다', '작다'); -- 크다
SELECT IF(100 > 200, '크다', '작다'); -- 작다
SELECT IFNULL(NULL, 'NULL값이다'); -- NULL값이다
SELECT IFNULL(100 + 300, 'NULL값이다.'); -- 400
SELECT NULLIF(50 + 50, 40 + 60); -- NULL
SELECT NULLIF(50 + 50, 40 + 40); -- 100

/* buyTbl 테이블에서 groupName 컬럼값이 NULL이면 자료없음으로 표시하여라 */
SELECT COUNT(*) FROM buyTbl;
SELECT * FROM buyTbl;
SELECT 
    prodName,
    IFNULL(groupName, '자료없음') AS groupName,
    price
FROM
    buyTbl;

-- 다중분기
-- CASE 값1 WHEN 값2 THEN 결과값1 ELSE 결과값2 END
-- 값1이 값2와 같다면 결과값1 그렇지 않다면 결과값2 반환
-- SET @age = CAST(10 AS SIGNED INTEGER);
SET @age = 5;
SELECT 
    CASE @age
        WHEN 0 THEN '영'
        WHEN 5 THEN '오'
        WHEN 10 THEN '십'
        ELSE '지정된 숫자가 아니다'
    END AS '결과';
    
/* @price 변수값에 따라 짝수, 홀수 출력하기 */
SET @price = 1;
SELECT 
    CASE @price % 2
        WHEN 0 THEN '짝수'
        ELSE '홀수'
    END AS '결과';
    
/* buyTbl 테이블에서 price 컬럼값에 따라 짝수, 홀수 출력하기 */
SELECT 
    price,
    CASE price % 2
        WHEN 0 THEN '짝수'
        ELSE '홀수'
    END AS '결과'
FROM
    buyTbl;
    
/* ------------------------------------------- */
-- 문자열 자료형 종류 p.231
-- CHAR(n), VARCHAR(n),
-- TINYTEXT, TEXT, MEDIUNTEXT,
-- LONGTEXT, BLOB, LONGBLOD

-- 여러 문자열을 하나의 문자열로 표시 p.241
-- 문자열 함수
-- CONCAT(EXP ...) : 문자열이나 테이블의 레코드를 함께 출력할 때 사용
-- CONCAT_WS(구분자, 문자열1, 문자열2 ... )
-- CONCAT_WS(구분자, 레코드1, 레코드2 ... )
-- : 문자열이나 레코드를 구분자와 함께 표시

SET @singer = '성시경';
SELECT CONCAT('거기 누구 없소...',' -- 이하이') AS '결과';
SELECT CONCAT('거리에서...', @singer) AS '결과';
SELECT 
    CONCAT_WS('/',
            '방탄소년단',
            '블랙핑크',
            '레드벨벳') AS '아이돌 그룹';

-- CONCAT() 이용해서 하나에 컬럼에 2개의 컬럼값 표시
-- 단가 X 수량 = 입금액
-- 적용전
SELECT * FROM buyTbl;
SELECT 
    num,
    price AS '가격',
    amount AS '수량',
    price * amount AS '구매액'
FROM
    buyTbl;

SELECT 
    num,
    CONCAT(CAST(price AS CHAR (7)),
            ' X ',
            CAST(amount AS CHAR (7)),
            ' = ') AS '단가 x 수량',
    price * amount AS '구매액'
FROM
    buyTbl;

-- 다음을 CONCAT을 사용하여 변경해보자 
-- SET @irm = '가수이름 =>';
-- SET @cm = 'cm';
-- SELECT @irm;
-- SELECT 
--     @irm AS ' ', name AS '이름', height AS '키', @cm AS ' '
-- FROM
--     userTbl
-- WHERE
--     height > 180;

-- 변수 사용
SET @irm = '가수이름 => ';
SET @cm ='cm';
SELECT 
    CONCAT(@irm, name) AS '이름', CONCAT(height, @cm) AS '키'
FROM
    userTbl;

-- 변수 사용 x, 문자열 사용
SELECT 
    CONCAT('가수이름 => ', name) AS '이름',
    CONCAT(height, 'cm') AS '키'
FROM
    userTbl;
    
-- 소숫점 자리 표시
-- FORMAT(숫자 자료형/필드명/수식, 소수점 자릿수)
SET @myNumber = 123.567890;
SELECT FORMAT(@myNumber, 1); -- 123.6
SELECT FORMAT(@myNumber, 4); -- 123.5679

--
SELECT * FROM buyTbl;
SELECT AVG(amount) FROM buyTbl; -- 3.3571
SELECT FORMAT(AVG(amount), 1) FROM buyTbl; -- 3.4

-- 특정 글자로 교체하기
-- INSERT(문자열, 시작위치, 길이, 교체문자열)
-- REPLACE(문자열, 원래문자열, 교체문자열)
SET @userPhone = "010-5555-6606";
SELECT INSERT(@userPhone, 5, 4, "####"); -- 010-####-6606
SELECT INSERT(@userPhone, 10, 4, "####"); -- 010-5555-####
SELECT REPLACE(@userPhone, "5555", "####"); -- 010-####-6606
SELECT INSERT(INSERT(@userPhone, 10, 4, '####'), 5, 4, "####"); -- 010-####-####

-- 특정 부분만 표시하기
-- LEFT(문자열, 길이), RIGHT(문자열, 길이)
-- : 왼쪽이나 오른쪽을 기준으로 길이만큼 잘라서 표시
-- SUBSTRING(문자열, 시작위치, 길이) : 시작위치에서 길이만큼 잘라서 표시한다.
SELECT @userPhone, LEFT(@userPhone, 3), RIGHT(@userPhone, 4);
SELECT @userPhone, LEFT(@userPhone, 3); -- 010-5555-6606	010
SELECT @userPhone, RIGHT(@userPhone, 3); -- 010-5555-6606	606
SELECT SUBSTRING(@userPhone, 5, 9); -- 5555-6606

-- LPAD(문자열, 길이, 채울 문자열), RPAD(문자열, 길이, 채울문자열)
-- : 왼쪽이나 오른쪽에 길이만큼 늘려 문자열을 채운다.
-- REPEAT(문자열, 반복횟수) : 문자열을 횟수만큼 반복한다.
SET @userName = "신짱구";
SELECT REPEAT(@userName, 3);
SELECT LPAD(@userName, 10, " * "), RPAD(@userName, 20, " * ");

-- 문자열 공백 없애기
-- LTRIM(문자열), RTRIM(문자열), TRIM(문자열)
SET @userM = "       근 하 신 년       ";
SELECT CONCAT('###',LTRIM(@userM), '###'); -- ###근 하 신 년       ###
SELECT CONCAT('###',RTRIM(@userM), '###'); -- ###       근 하 신 년###
SELECT CONCAT('###',TRIM(@userM), '###');  -- ###근 하 신 년###

/* userTbl 테이블에서 name 필드 값을 다음과 같이 표시하여라
                         홍**                       */
SELECT name FROM userTbl;
SELECT INSERT(name, 2, 2, '**') AS '홍**' FROM userTbl;

/* userTbl 테이블에서 name 필드값이 조로 시작하는 문자열을 다음과 같이 변경하여라 
조관우 회원님
조용필 회원님       */

SELECT name FROM userTbl;
SELECT RPAD(name, 7, " 회원님") AS '회원 목록' FROM userTbl;

-- 날짜 자료형 종류
-- p.232 p.248
-- YEAR, DATE, TIME, DATEITME

-- 문자열 => 날짜형
SELECT CAST('2020-12-12 12:12:12' AS DATE) AS DATE; -- 2020-12-12
SELECT CAST('2019-12-25 12:12:12' AS DATETIME); -- 2019-12-25 12:12:12
SELECT CAST('2019-12-25 12:12:12' AS TIME) AS TIME; -- 12:12:12

-- 현재 시간과 날짜 출력
-- NOW() : 내장함수로 현재의 날짜와 시간을 표시
-- SYSDATE() : 내장함수로 현재의 날짜와 시간을 표시
-- CURDATE() : 현재 날짜 표시
-- CURTIME() : 현재 시간 표시
SELECT NOW();
SELECT 
    NOW(),
    CAST(NOW() AS DATE) AS '현재 날짜',
    CAST(NOW() AS TIME) AS '현재 시각';

SELECT 
    SYSDATE(),
    CAST(SYSDATE() AS DATE) AS '현재 날짜',
    CAST(SYSDATE() AS TIME) AS '현재 시각';

SELECT 
    SYSDATE(),
    CURDATE() AS '현재 날짜',
    CURTIME() AS '현재 시각';

CREATE TABLE timeTable
(tYear YEAR, tDay DATE, tTime TIME, tDateTime DATETIME);
DESC timeTable;
SELECT * FROM timeTable;
INSERT INTO timeTable (tYear, tDay, tTime, tDateTime)
VALUES (CURDATE(), CURDATE(),CURTIME(),SYSDATE());

SELECT '오늘은', YEAR(NOW()), '년', MONTH(NOW()), '월', DAY(now()), '일입니다.';

-- HOUR(시간), MINUTE(시간), SECOND(시간), TIME(시간)
SELECT 
	YEAR(NOW()) AS 'YEAR',
	MONTH(NOW()) AS 'MONTH',
	DAY(NOW()) AS 'DAY',
    HOUR(NOW()) AS 'HOUR',
    MINUTE(NOW()) AS 'MINUTE',
    SECOND(NOW()) AS 'SECOND';
    
-- DAYOFWEEK(날짜) : 요일표시 1~7 (일~토)
-- MONTHNAME(날짜) : 달을 영문으로 표시
-- DAYOFYEAR(날짜) : 1년 중 몇번째 날인지 표시
SELECT DAYOFWEEK(NOW()), MONTHNAME(NOW()), DAYOFYEAR(NOW());

/* CASE문을 이용하여 요일 표시하기 */
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

-- 날짜 연산 함수
-- DATEDIFF(날짜1, 날짜2) : 날짜1 - 날짜2
-- TIMEDIFF(시간1, 시간2) : 시간1 - 시간2

SELECT DATEDIFF('2021-01-01',NOW());
SELECT TIMEDIFF('17:50:00', CURTIME());

SELECT DATEDIFF(NOW(),'2019-11-05');

/* ------------------------------------------- */
-- 시스템 함수 p.251
-- DATABASE() 사용중인 데이터베이스 표시
-- USER() 사용자 표시
-- VERSION() MySQL 버전 표시
SELECT 
    DATABASE() AS '데이터베이스',
    USER() AS '사용자',
    VERSION() AS 'MySQL 버전';