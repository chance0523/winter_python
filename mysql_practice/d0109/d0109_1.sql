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
