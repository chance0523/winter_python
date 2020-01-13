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

