-- 테이블 뷰 p.339
-- 원본 테이블 데이터는 그래도 유지
-- 필요한 필드만 모아서 별도의 뷰라는 테이블로 구성
-- 목적 : 보안
-- 테이블처럼 CRUD 가능

-- 뷰 생성
USE sqlDB;
-- userTbl 테이블에서 id, name, addr => v_userTbl 뷰 생성
CREATE VIEW v_userTbl AS
SELECT userID, name, addr FROM userTbl;

desc userTbl;
desc v_userTbl;
SELECT * FROM v_userTbl;

-- 뷰 삭제하기
-- DROP VIEW 뷰이름
DROP VIEW v_userTbl;

-- 뷰에 데이터 삽입하기
-- 뷰에 등록된 필드의 데이터만 삽입가능
CREATE VIEW v_userTbl AS
SELECT userID, name, birthYear,addr FROM userTbl;

SELECT COUNT(*) FROM v_userTbl; -- 10

/*
INSERT INTO 뷰이름
  (필드명1 ... ) VALUES (데이터값1 ... );
INSERT INTO 뷰이름
  VALUES (데이터값1 ... );
INSERT INTO 뷰이름
  VALUES(데이터값1 ...), (데이터값2 ...), ... ;
*/
DESC v_userTbl;
INSERT INTO v_userTbl VALUES ('ASS','안성수',2009,'부산');
SELECT * FROM v_userTbl;
SELECT * FROM userTbl; -- 원본에도 들어감

-- 뷰의 데이터 수정
/*
UPDATE 뷰이름 SET 필드명 = 값 WHERE 절;
*/
SELECT * FROM v_userTbl;
UPDATE v_userTbl SET addr = '서울';
SELECT * FROM userTbl; -- 원본에도 수정

-- 뷰에서 레코드 삭제하기
/*
DROP FROM 뷰이름 WHERE 절;
*/
-- 가장 최근에 삽입한 레코드 삭제하기
DELETE FROM v_userTbl WHERE name = '안성수';
SELECT * FROM v_userTbl;
SELECT * FROM userTbl; -- 원본에서도 삭제

-- AS 별칭 가능한가?
SELECT * FROM v_userTbl;
SELECT name AS '이름(name)', addr AS '지역(addr)' FROM v_userTbl WHERE addr = '서울';

-- 집계함수(MIN/MAX/COUNT/SUM)랑 계산식 확인
SELECT * FROM buyTbl;
SELECT price AS '가격', amount AS '갯수', price*amount AS '총합' FROM buyTbl;
-- 1) v_buyTbl1 뷰 생성하기
-- 원본 필드의 필수 항목 확인하기
desc buyTbl;
-- 2) 원본필드의 필수항목으로 뷰 만들기
CREATE VIEW v_buyTbl AS SELECT num, userID, prodName, price, amount, price*amount FROM buyTbl;
SELECT * FROM v_buyTbl;
-- 3) 뷰에서 price*amount 수식으로 이루어진 필드 생성되는지 확인하기
-- 4) 뷰에서 레코드 전체 갯수 count()되는지 확인하기
select count(*) from v_buyTbl;
-- 5) 뷰에서 price 필드의 평균값 확인하기 AVG()
select price, amount, AVG(price) from v_buyTbl;
select count(*), format(AVG(price),1) from v_buyTbl;

-- 조인의 결과를 뷰로 생성하기
/*
CREATE VIEW 뷰이름 AS
  ( 조인 명령문 );
*/
-- userTbl / buyTbl INNER JOIN해서 뷰로 등록하기
/*
SELECT 필드명
  FROM 테이블1 별칭1
  INNER JOIN 테이블2 별칭2
  ON 별칭1.필드명1 = 별칭2.필드명2;
*/

DESC userTbl;
DESC buyTbl;

SELECT U.userId, name, addr, concat(mobile1,'-',mobile2) AS 'phone number', prodName, price, amount
  FROM userTbl U
  INNER JOIN buyTbl B
  ON U.userId = B.userID;
  
-- 뷰로 등록하기
CREATE VIEW v_buyTbl_userTbl AS
(SELECT U.userId, name, addr, concat(mobile1,'-',mobile2) AS 'phone number', prodName, price, amount
  FROM userTbl U
  INNER JOIN buyTbl B
  ON U.userId = B.userID);

SELECT * FROM v_buyTbl_userTbl;


-- quiz
/*
1. worldTestDB 데이터베이스 만들기
2. world 데이터베이스의 country, countrylanguage 테이블을
   worldTestDB 데이터베이스에 복사하기
3. country, countrylanguage 테이블 INNER JOIN 하기
-- 출력형태
  countrycode / name / population / language / isoffical 
*/
-- 1. worldTestDB 데이터베이스 만들기
CREATE DATABASE worldTestDB; 
USE worldTestDB;
-- 2. world 데이터베이스의 country, countrylanguage 테이블을 worldTestDB 데이터베이스에 복사하기
CREATE TABLE country (SELECT * FROM world.country);
CREATE TABLE countrylanguage (SELECT * FROM world.countrylanguage); 
-- 3. country, countrylanguage 테이블 INNER JOIN 하기
SELECT * FROM country; -- code, name, population ...
SELECT * FROM countrylanguage; -- countrycode, language, isofficial ...

SELECT 
    C.Code AS 'countrycode',
    C.Name AS 'Name',
    C.Population AS 'Population',
    CL.Language AS 'Language',
    CL.IsOfficial AS 'IsOfficial'
FROM
    country C
        INNER JOIN
    countrylanguage CL ON C.Code = CL.CountryCode;

CREATE VIEW v_country_contrylanguage AS
(SELECT 
    C.Code AS 'countrycode',
    C.Name AS 'Name',
    C.Population AS 'Population',
    CL.Language AS 'Language',
    CL.IsOfficial AS 'IsOfficial'
FROM
    country C
        INNER JOIN
    countrylanguage CL ON C.Code = CL.CountryCode);
    
SELECT * FROM v_country_contrylanguage;

