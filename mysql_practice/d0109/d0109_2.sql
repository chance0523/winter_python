USE sqldb;
-- GROUP BY + 집계함수
-- SUM(컬럼명) , AVG(컬럼명)
-- 컬럼명 AS 별칠 : 컬럼명의 필드명을 별칭으로 표시
-- buyTbl 테이블에서 price의 합계와 평균을 출력하여라
DESC buyTbl;
SELECT SUM(price) FROM buyTbl;
SELECT SUM(price) AS '합계' FROM buyTbl; -- 변한건 아니고 화면에 뿌려줄때만
SELECT AVG(price) AS '평균' FROM buyTbl;
SELECT SUM(price) AS '합계', AVG(price) AS '평균' FROM buyTbl;

-- 그룹 이름별로 합계와 평균 구하기
SELECT * FROM buyTbl;
SELECT groupName, SUM(price) AS '합계' , AVG(price) AS '평균' FROM buyTbl GROUP BY groupName ORDER BY groupName;

-- quiz
-- buyTbl에서 사용자별로 구매 합계를 구해보세요
SELECT DISTINCT userID FROM buyTbl;
SELECT userID, SUM(price*amount) AS '합계' FROM buyTbl GROUP BY userID;

SELECT MIN(height) AS '최소값', MAX(height) AS '최대값' FROM userTbl;

-- SELECT name, MIN(height) AS '최소값', MAX(height) AS '최대값' FROM userTbl;
SELECT name, height FROM userTbl
WHERE height = (SELECT MAX(height) FROM userTbl)
   OR height = (SELECT MIN(height) FROM userTbl);

-- userTbl 테이블에서 휴대폰 사용자수와 휴대폰이 없는 사용자 수 표시하기
DESC userTbl;
SELECT * FROM userTbl;
-- 휴대폰 사용자 수
SELECT COUNT(mobile1) AS '휴대폰 사용자 수' FROM userTbl;
-- 휴대폰이 없는 사용자 수 : 전체 사용자 수 - 휴대폰 사용자 수
SELECT COUNT(*) - COUNT(mobile1) AS '휴대폰 미사용자 수' FROM userTbl;

SELECT
COUNT(*) AS '총 user 수',
COUNT(mobile1) AS '휴대폰 사용자 수',
COUNT(*) - COUNT(mobile1) AS '휴대폰 미사용자 수'
FROM userTbl;

-- p.213 HAVING 절
-- 집계 함수를 이용하여 컬럼값 => 조건

-- buyTbl 에서 사용자별(GROUP BY) 총 구매액(price*amount)
SELECT userID AS '사용자 아이디',
	   SUM(price*amount) AS '총구매액'
       FROM buyTbl GROUP BY userID;
       
-- buyTbl 에서 사용자별(GROUP BY) 총 구매액(price*amount)에서
-- 조건 적용 : 총구매액이 1000보다 큰 레코드만 출력해라
SELECT userID AS '사용자 아이디',
	   SUM(price*amount) AS '총구매액'
       FROM buyTbl
       -- WHERE SUM(price*amount) > 1000 은 불가 !!!
       GROUP BY userID
       HAVING SUM(price*amount) > 1000;

-- quiz : buyTbl에서 사용자 아이디 별로 평균 구매 횟수가 1~3인 레코드만 출력하여라
-- AVG, GROUP BY, HAVING, BETWEEN 이용
SELECT userID, AVG(amount) FROM buyTbl
	   GROUP BY userID
       HAVING AVG(amount) BETWEEN 1 AND 3
       ORDER BY AVG(amount);
       
-- p214 WITH ROLLUP : 중간합계
-- buyTbl 테이블에서 groupName 별로 합계 출력
SELECT groupName, SUM(price*amount) AS '비용' FROM buyTbl GROUP BY groupName;
SELECT groupName, SUM(price*amount) AS '비용' FROM buyTbl GROUP BY groupName WITH ROLLUP;

-- 레코드 삽입1
-- INSERT INTO 테이블명 (컬럼명) VALUES (값)
SELECT * FROM buyTbl;
INSERT INTO buyTbl (userID, prodName, groupName, price, amount)
			  VALUE('KBS', 'Python', '컴퓨터', 5000, 6);
              
-- 레코드 삽입2
-- num => 자동숫자증감/NULL
-- INSERT INTO 테이블명 VALUES (값)
INSERT INTO buyTbl VALUE(NULL, 'KBS', 'Python', '컴퓨터', 5000, 6);

-- 레코드 삽입3
-- 다른 테이블의 레코드를 이용해서 삽입
-- INSERT INTO 테이블명1 (컬럼명) (SELECT 컬럼명 FROM 테이블명2 WHERE절);
CREATE TABLE buyTbl2
( num		INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  userID	CHAR(8) NOT NULL,
  prodName	CHAR(6) NOT NULL,
  groupName	CHAR(4),
  price		INT NOT NULL,
  amount	SMALLINT NOT NULL
);

SELECT * FROM buyTbl2;
-- buyTbl의 groupName 값이 '전자' 레코드 => buyTbl
INSERT INTO buyTbl2 (userId, prodName, groupName, price, amount)
            (SELECT userId, prodName, groupName, price, amount FROM buyTbl WHERE groupName = '전자');

