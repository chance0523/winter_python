-- ######################################
-- 스토어드 프로시저 (Stored Procedure) (p.415)
-- 쿼리문의 집합. 함수와 비슷

-- 스토어드 프로시저 기본 템플릿 정의 

/*
DROP PROCEDURE IF EXISTS 스토어드프로시저이름; 
DELIMITER $$
CREATE PROCEDURE 스토어드프로시저이름()
BEGIN

SQL 프로그래밍 (IF, CASE, WHILE..)

END $$
DELIMITER ;
*/

-- ######################################
-- 스토어드 프로시저 테스트 1
-- 생성된 스토어드 프로시저는 
-- [Navigator] 탭의 관련 DB 목록 아래의 Stored Procedures 에서 확인 
-- 변수를 선언하고 출력한다. 

USE worldtestdb;
DROP PROCEDURE IF EXISTS varTest;
DELIMITER $$
CREATE PROCEDURE varTest()
BEGIN
  SELECT 'hello world';
  -- 변수 선언 후 출력하기
  SET @message = 'hello SQL';
  SELECT @message; -- hello SQL만 출력된다.
  -- 테이블의 레코드를 조회해서 출력하기
  SELECT * FROM country LIMIT 10;
END $$
DELIMITER ;

-- 스토어드프로시저 호출 명령 
/*
CALL 스토어드프로시저이름();
*/
CALL varTest();

-- ######################################
-- 매개변수가 있는 스토어드 프로시저  
-- CREATE PROCEDURE 프로시저이름(IN 매개변수이름1 자료형 ,IN 매개변수이름2 자료형) --

-- 프로시저 호출시 
-- CALL 프로시저이름(전달값);

DROP PROCEDURE IF EXISTS paramTest1;
DELIMITER $$
CREATE PROCEDURE paramTest1(IN myNum INT(3))
BEGIN
-- 매개변수를 출력하기
  SELECT CONCAT('현재 변수 값 : ', myNum) AS '결과';
END $$
DELIMITER ;

CALL paramTest1(10);
CALL paramTest1(100);

DROP PROCEDURE IF EXISTS paramTest2;
DELIMITER $$
CREATE PROCEDURE paramTest2(IN myNum INT(3), myName VARCHAR(10))
BEGIN
-- 매개변수를 출력하기
  SELECT CONCAT('myNum = ', myNum, ' myName = ', myName) AS '결과';
END $$
DELIMITER ;

CALL paramTest2(100,'홍길동');
CALL paramTest2(700,'신데렐라');


-- quiz. calPro(num1, num2)
-- 출력형태
-- num1  num2  +  -  *  /
DROP PROCEDURE IF EXISTS calPro;
DELIMITER $$
CREATE PROCEDURE calPro(IN num1 INT(3), num2 INT(3))
BEGIN
SELECT 
    num1,
    num2,
    CONCAT(num1 + num2) AS '+',
    CONCAT(num1 - num2) AS '-',
    CONCAT(num1 * num2) AS '*',
    FORMAT(CONCAT(num1 / num2), 2) AS '/';
END $$
DELIMITER ;

CALL calPro(10, 5)



-- ######################################
--  p283
-- 조건에 따라 분기 
/*
IF 조건식 THEN
    명령문1
ELSE
    명령문2
END IF;
*/

DROP PROCEDURE IF EXISTS ifTest1;
DELIMITER $$
CREATE PROCEDURE ifTest1()
BEGIN
  SET @num = 100;
  IF @num > 100 THEN
      SELECT '100보다 크다';
  ELSE
      SELECT '100보다 작거나 같다';
  END IF;
END $$
DELIMITER ;

CALL ifTest1();