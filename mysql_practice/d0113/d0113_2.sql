-- 테이블 구조 변경
-- 필드 추가 / 삭제
-- 필드명 변경
-- 외래키나 기본키 추가 / 삭제

use sqldb;
-- sqlDB 데이터베이스에서
-- buyTbl => buyTbl_aa
-- userTbl => userTbl_aa

CREATE TABLE buyTbl_aa (SELECT * FROM buyTbl);
CREATE TABLE userTbl_aa (SELECT * FROM userTbl);

-- 기존 테이블에 필드 추가하기
/*
ALTER TABLE 테이블명
  ADD 필드명 데이터형
    (DEFAULT 초기값)
      (NULL / NOT NULL);
*/

-- userTbl_aa 에 homePage(VARCHAR(30)) 필드 추가하기
ALTER TABLE userTbl_aa
ADD homePage VARCHAR(30)
DEFAULT 'http://google.com'
NULL;

SELECT * FROM userTbl_aa;

ALTER TABLE userTbl_aa
ADD age INT(3)
NULL;

-- 기존 테이블의 필드명 교체
/*
ALTER TABLE 테이블명
  CHANGE COLUMN 컬럼명1 컬럼명2 데이터형
    (NULL / NOT NULL);
*/
ALTER TABLE userTbl_aa
CHANGE COLUMN age userAge INT(3);

-- 기존 테이블의 필드 삭제
/*
ALTER TABLE 테이블명
  DROP COLUMN 필드명;
*/

DESC usertbl_aa;
ALTER TABLE userTbl_aa
DROP COLUMN height;
desc usertbl_aa;

/* ---------------------------------- */
-- 기본키 (Primary) 추가하기
-- 필드값에 중복값이 없어야한다.
/*
ALTER TABLE 테이블명
  ADD CONSTRAINT 기본키명(PK_테이블명_필드명)
  PRIMARY KEY(필드명)
*/

DESC USERTBL_AA;
-- userTbl_aa 테이블에서 userID를 기본키로 설정하기
ALTER TABLE userTbl_aa
  ADD CONSTRAINT PK_userTbl_aa_userID
  PRIMARY KEY(userID);
  
-- 기본 키 삭제
/*
ALTER TABLE 테이블명
  DROP PRIMARY KEY;
*/
ALTER TABLE userTbl_aa
  DROP PRIMARY KEY;
  
/* ---------------------------------- */
-- 외래 키 추가하기
-- 외부테이블의 외래키로 참조할 필드명이 현재 테이블에 있어야한다.
-- 외래키는 MUL로 표시

/*
ALTER TABLE 테이블명
  ADD CONSTRAINT 외래키명(FK_테이블명_필드)
  FOREIGN KEY (필드명)
  REFERENCES 참조테이블(필드명);
*/
show tables;
desc userTbl_aa;
desc buyTbl_aa;
-- buytbl_aa 테이블의 userID 외래키로 지정
-- 외래키 참조 테이블의 필드명 usertlb_aa의 userID
ALTER TABLE buyTbl_aa
  ADD CONSTRAINT FK_userTbl_aa_buyTbl_aa
  FOREIGN KEY (userID)
  REFERENCES userTbl_aa(userID);
  
desc buyTbl_aa;
show index from userTbl_aa;
show index from buyTbl_aa;

-- 외래 키 삭제하기
-- 외래키명은 SCHEMAS에서 확인
/*
ALTER TABLE 테이블명
  DROP FOREIGN KEY 외래키명;
*/
ALTER TABLE buyTbl_aa
  DROP FOREIGN KEY FK_userTbl_aa_buyTbl_aa;
desc buyTbl_aa;
-- desc나 index에서는 그대로인데 shemas에서만 삭제?
use employees;
use sqldb;

/*
quiz
1) employees 데이터베이스로 접속
2) employees 테이블에서
emp_no, first_name, last_name, gender
10개의 레코드 복사해서 employees_table 생성
3) employees_test 테이블에 컬럼추가
  State (VARCHAR(30))
    디폴트값은 'Hawaii'로 지정
4) employees_test 테이블에서 gender 컬럼 삭제
5) employees_test 테이블에서 last_name을 family_name으로 변경
6) employees_test 테이블에서 기본키는 emp_no으로 지정
*/
CREATE TABLE employees_test (SELECT emp_no,first_name,last_name,gender FROM employees limit 10); -- 테이블 생성
select * from employees_test;

ALTER TABLE employees_test
ADD COLUMN State VARCHAR(30)
DEFAULT 'Hawaii'; -- state 컬럼 추가

ALTER TABLE employees_test DROP COLUMN gender; -- gender 컬럼 삭제

ALTER TABLE employees_test
CHANGE COLUMN last_name family_name VARCHAR(16); -- last_name 컬럼명을 family_name으로 변경

ALTER TABLE employees_test
  ADD CONSTRAINT PK_employees_test_emp_no
    PRIMARY KEY (emp_no); -- emp_no을 PRIMARY KEY로 설정

desc employees_test;