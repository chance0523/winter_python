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
-- CONVERT ( ... AS 데이터형식)
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
SELECT CAST('2nd123' AS SIGNED INTEGER); -- 2
