--  퀴즈 - 
USE sqldb;
-- 1) buyTbl 테이블의 구조 확인하기 
DESCRIBE buytbl;
-- 2) buyTbl 테이블에서 userID, prodName 컬럼만 출력하기 
SELECT userID, prodName FROM buyTbl;
-- 3) buyTbl 테이블에서 userID가 'KBS'인 레코드 출력하기 
SELECT * FROM buyTbl WHERE userID = 'KBS';
-- 4) buyTbl 테이블에서 prodName 컬럼을 중복없이 출력하기 
SELECT DISTINCT prodName FROM buyTbl; 
-- 5) buyTbl 테이블에서 groupName이 NULL인 레코드 출력하기 (IS NULL 이용)
SELECT * FROM buyTbl WHERE groupName IS NULL;
-- 6) buyTbl 테이블에서 amount가 5보다 큰 레코드 출력하기 
SELECT * FROM buyTbl WHERE amount > 5;
-- 7) buyTbl 테이블에서 prodName 컬럼이 '청바지' 이거나 '운동화'인 레코드 출력구문을 2가지로 방법으로 작성하기 
-- (OR, IN 사용)
SELECT * FROM buyTbl WHERE prodName = '청바지' OR prodName = '운동화';
SELECT * FROM buyTbl WHERE prodName IN ('청바지','운동화'); 
-- 8) buyTbl 테이블에서 price 컬럼값이 30~80인 레코드 출력구문을 2가지 방법으로 작성하기 
-- (AND 구문, BETWEEN .. AND 구문 이용)
SELECT * FROM buyTbl WHERE price >= 30 AND price <= 80;
SELECT * FROM buyTbl WHERE price BETWEEN 30 AND 80;
-- 9) buyTbl 테이블에서 userID에 'K'로 시작하는 레코드 출력하기 (LIKE 이용)
SELECT * FROM buyTbl WHERE userId LIKE 'K%';
-- 10) buyTbl 테이블에서 prodName이 ??화로 끝나는 레코드 출력하기 (LIKE 이용)
SELECT * FROM buyTbl WHERE prodName LIKE '__화';

-- 11) buyTbl 테이블에서 userID 컬럼값이 'JYP'인 price 컬럼값 보다 큰 레코드 출력하기
-- (서브쿼리 이용)
SELECT * FROM buyTbl WHERE price > (SELECT price FROM buyTbl WHERE userID = 'JYP');
    
-- 12) buyTbl 테이블에서 userID 컬럼값이 'JYP'인 amount 컬럼값과 같은 레코드 출력하기 
-- (서브쿼리 이용)
SELECT * FROM buyTbl WHERE amount = (SELECT amount FROM buyTbl WHERE userID = 'JYP');

-- 13) buyTbl 테이블에서 price 컬럼값이 큰 순서대로 5개만 출력하기 
-- (ORDER BY, LIMIT) 이용
SELECT * FROM buyTbl ORDER BY price DESC LIMIT 5;

-- 14) buyTbl 테이블에서 userID 컬럼값이 'KBS'인 레코드 목록 중 price 컬럼값이 가장 작은 레코드 출력하기 
-- (WHERE, ORDER BY, LIMIT) 이용
SELECT * FROM buyTbl WHERE userID = 'KBS' ORDER BY price LIMIT 1;

-- 15) userTbl 테이블에서 addr 컬럼값이 '서울'인 레코드만 복사해서 새로운 테이블 userTbl1 생성하기 
-- (CREATE TABLE ~) 이용
CREATE TABLE userTbl1 (SELECT * FROM userTbl WHERE addr = '서울');
SELECT * FROM userTbl1;

-- 16) userTbl 테이블에서 name 컬럼값이 '은지원'인 레코드의 height 컬럼값보다 
--  큰 레코드만 height 값을 기준으로 정렬하여 복사해서 새로운 테이블 userTbl2 생성하기. 
-- (CREATE TABLE ~) 이용
CREATE TABLE userTbl2 (SELECT * FROM userTbl WHERE height > (SELECT height FROM userTbl WHERE name = '은지원')); 
SELECT * FROM userTbl2;