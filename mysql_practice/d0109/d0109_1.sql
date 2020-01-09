use world;
-- 주석
/*
여러줄
주석
*/
-- USE employees;
-- 데이터베이스의 목록 확인
SHOW DATABASES;
-- 데이터베이스의 테이블 목록 확인
SHOW TABLES;
-- 접속중인 데이터베이스의 테이블 목록의 정보 확인하기
SHOW TABLE STATUS;
-- 특정 테이블의 정보 확인하기
-- DESCRIBE 테이블명;
-- DESC 테이블명;
-- DESCRIBE(/DESC) 데이터베이스명.테이블명;
DESCRIBE city;
DESC country;
DESCRIBE employees.salaries;

SELECT * FROM city;
SELECT * FROM employees.salaries;
SELECT * FROM employees.departments LIMIT 10;
SELECT Name, Population FROM city LIMIT 10;

/* ----------------------------- */
-- 새 데이터베이스 만들기 p.193
-- 데이터베이스 생성하기
-- CREATE DATABASE 데이터베이스명 (IF NOT EXISTS 데이터베이스명)
CREATE DATABASE sqlDB;
SHOW DATABASES;
USE sqlDB;

-- 테이블 만들기
-- CREATE TABLE 테이블명(필드명 자료형 옵션, ... );
-- userTbl 생성
CREATE TABLE userTbl
( userID	CHAR(8) NOT NULL PRIMARY KEY,
  name		VARCHAR(10) NOT NULL,
  birthYear	INT NOT NULL,
  addr		CHAR(2) NOT NULL,
  mobile1	CHAR(3),
  mobile2	CHAR(8),
  height	SMALLINT,
  mDate		DATE
);
SHOW TABLES;
SELECT * FROM userTbl;

-- buyTbl 생성
CREATE TABLE buyTbl
( num		INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  userID	CHAR(8) NOT NULL,
  prodName	CHAR(6) NOT NULL,
  groupName	CHAR(4),
  price		INT NOT NULL,
  amount	SMALLINT NOT NULL,
  FOREIGN KEY (userID) REFERENCES userTbl(userID)
);
SHOW TABLES;
SELECT * FROM buyTbl;

-- userTbl 테이블의 레코드 삽입 
-- INSERT INTO userTbl VALUES('LSG', '이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8');
-- INSERT INTO userTbl VALUES('KBS', '김범수', 1979, '경남', '011', '2222222', 173, '2012-4-4');
-- INSERT INTO userTbl VALUES('KKH', '김경호', 1971, '전남', '019', '3333333', 177, '2007-7-7');
-- INSERT INTO userTbl VALUES('JYP', '조용필', 1950, '경기', '011', '4444444', 166, '2009-4-4');
-- INSERT INTO userTbl VALUES('SSK', '성시경', 1979, '서울', NULL  , NULL      , 186, '2013-12-12');
-- INSERT INTO userTbl VALUES('LJB', '임재범', 1963, '서울', '016', '6666666', 182, '2009-9-9');
-- INSERT INTO userTbl VALUES('YJS', '윤종신', 1969, '경남', NULL  , NULL      , 170, '2005-5-5');
-- INSERT INTO userTbl VALUES('EJW', '은지원', 1972, '경북', '011', '8888888', 174, '2014-3-3');
-- INSERT INTO userTbl VALUES('JKW', '조관우', 1965, '경기', '018', '9999999', 172, '2010-10-10');
-- INSERT INTO userTbl VALUES('BBK', '바비킴', 1973, '서울', '010', '0000000', 176, '2013-5-5');

-- buyTbl 테이블의 레코드 삽입 
-- INSERT INTO buyTbl VALUES(NULL, 'KBS', '운동화', NULL   , 30,   2);
-- INSERT INTO buyTbl VALUES(NULL, 'KBS', '노트북', '전자', 1000, 1);
-- INSERT INTO buyTbl VALUES(NULL, 'JYP', '모니터', '전자', 200,  1);
-- INSERT INTO buyTbl VALUES(NULL, 'BBK', '모니터', '전자', 200,  5);
-- INSERT INTO buyTbl VALUES(NULL, 'KBS', '청바지', '의류', 50,   3);
-- INSERT INTO buyTbl VALUES(NULL, 'BBK', '메모리', '전자', 80,  10);
-- INSERT INTO buyTbl VALUES(NULL, 'SSK', '책'    , '서적', 15,   5);
-- INSERT INTO buyTbl VALUES(NULL, 'EJW', '책'    , '서적', 15,   2);
-- INSERT INTO buyTbl VALUES(NULL, 'EJW', '청바지', '의류', 50,   1);
-- INSERT INTO buyTbl VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2);
-- INSERT INTO buyTbl VALUES(NULL, 'EJW', '책'    , '서적', 15,   1);
-- INSERT INTO buyTbl VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2);

-- 테이블 조회
SELECT * FROM userTbl;
SELECT * FROM buyTbl;
SELECT COUNT(*) FROM userTbl;  -- 10
SELECT COUNT(*) FROM buyTbl;  -- 12

/* ------------------------------ */
-- FILTERING : 조건에 맞는 레코드 출력하기
-- WHERE 조건절의 연산자는? 관계연산자(>, = , ...), 논리연산자(AND, OR NOT)
-- userTbl 테이블에서 김경호만 출력하기
SELECT * FROM userTbl WHERE name = '김경호';
-- userTbl 테이블에서 birthYear가 1970보다 크거나 같고 height이 182보다 작다
SELECT * FROM userTbl WHERE birthYear >= 1970 AND height < 182;

-- userTbl 테이블에서 180<=height<=183 인 userId, name 출력하기
SELECT userID, name FROM userTbl WHERE height>=180 AND height<=183;

-- 범위를 지정할 때 사용하는 연산자 BETWEEN
-- BETWEEN 값1 AND 값2 : 값1 ~ 값2
SELECT userID, name FROM userTbl WHERE height BETWEEN 180 AND 183;
SELECT COUNT(*) FROM userTbl WHERE height BETWEEN 180 AND 183; -- 2

-- 해당 값에 해당하는 레코드 추출 : IN 연산자
-- 컬럼명 IN(값1, 값2 ...)
-- userTbl 에서 addr 컬럼값이 경남, 전남, 경북인 레코드 출력
SELECT COUNT(*) FROM userTbl WHERE addr = '경남' OR addr = '전남' OR addr = '경북'; -- 4
SELECT COUNT(*) FROM userTbl WHERE addr IN ('경남','전남','경북'); -- 4

-- LIKE 연산자
-- 문자열이나 값 검색
-- LIKE ..%( )
-- LIKE _( )
SELECT COUNT(*) FROM userTbl WHERE name LIKE '김%'; -- 2
SELECT COUNT(*) FROM userTbl WHERE name LIKE '김__'; -- 2
SELECT COUNT(*) FROM userTbl WHERE name LIKE '김_'; -- 0   _ 의 갯수에 따라 달라짐
SELECT * FROM userTbl WHERE name LIKE '_종신'; -- 윤종신

-- userTbl에서 addr 지역명이 '경'으로 시작하거나 '남'으로 끝나는 레코드 출력
SELECT * FROM userTbl WHERE addr LIKE '경%' OR '%남';

/* ---------------------------------- */
-- 서브쿼리 (Sub Query)
-- 쿼리문 안에 쿼리문이 들어가는 것
-- SELECT .. FROM .. WHERE 조건절1 (SELECT .. FROM .. WHERE 조건절2)
-- 주의 사앟 : 서브쿼리의 레코드 결과값은 1개로 유일해야한다.

-- userTbl 테이블에서 height  컬럼값이 177 이상인 레코드
SELECT * FROM userTbl WHERE height > 177;

-- 177을 또다른 쿼리문으로 대치
-- 김경호의 키를 모른다는 가정
-- 주의사항 : 서브쿼리의 경우 레코드가 하나만 추출되어야 한다.
SELECT height FROM userTbl WHERE name = '김경호';

-- 김경호보다 키가 큰 사람의 이름과 키를 출력하여라
SELECT name, height FROM userTbl WHERE height > (SELECT height FROM userTbl WHERE name = '김경호');

-- 서브쿼리의 레코드가 다중인 경우 : ANY (서브쿼리문)
-- 지역이 경남인 사람의 키보다 크거나 같은 사람의 이름과 키를 출력하여라
SELECT height FROM userTbl WHERE addr = '경남';
SELECT name, height FROM userTbl WHERE height >= ANY (SELECT height FROM userTbl WHERE addr = '경남');

-- 정렬 ORDER BY 컬럼명 ASC/DESC
SELECT * FROM userTbl ORDER BY birthYear;
SELECT * FROM userTbl ORDER BY birthYear DESC;

-- addr을 기준, 두번째 조건을 name으로
SELECT * FROM userTbl ORDER BY addr;
SELECT * FROM userTbl ORDER BY addr, name;

-- 레코드 값의 중복 제거
-- addr 컬럼값의 구성 표시 (중복값없이)
SELECT addr FROM userTbl;
SELECT DISTINCT addr FROM userTbl;

/* ----------------------------------- */
-- 기존 테이블의 특정 컬럼을 복사해서 새로운 테이블 만들기
-- CREATE TABLE 새로운 테이블명 (SELECT 복사할 열 FROM 기존테이블)
-- buyTbl에서 전체 복사 => buyTbl_a
CREATE TABLE buyTbl_a (SELECT * FROM buyTbl);
SHOW TABLES;
SELECT * FROM buyTbl_a;
-- buyTbl에서 일부 열만 복사 => buyTbl_b
CREATE TABLE buyTbl_b (SELECT userID, prodName FROM buyTbl);
SHOW TABLES;
SELECT * FROM buyTbl_b;

-- userTbl에서 addr이 '서울' => userTbl_seoul
CREATE TABLE userTbl_seoul (SELECT * FROM userTbl WHERE addr = '서울');
SHOW TABLES;
SELECT * FROM userTbl_seoul;