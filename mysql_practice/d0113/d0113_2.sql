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

-- 기존 테이블에 필드명 교체
/*
ALTER TABLE 테이블명
  CHANGE COLUMN 컬럼명1 컬럼명2 데이터형
    (NULL / NOT NULL);
*/
ALTER TABLE userTbl_aa
CHANGE COLUMN age userAge INT(3);