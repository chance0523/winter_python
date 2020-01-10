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