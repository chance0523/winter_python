USE SQLDB;

-- 다중 IF
/*
IF 조건식 THEN
  명령문1
ELSEIF 조건식 THEN
  명령문2
ELSE
  명령문3
END IF;
*/
DROP PROCEDURE IF EXISTS ifProc_para;
DELIMITER $$
CREATE PROCEDURE ifProc_para(IN point INT)
BEGIN
  DECLARE credit CHAR(1);
  IF point >= 90 THEN
    SET credit = 'A';
  ELSEIF point >= 80 THEN
    SET credit = 'B';
  ELSEIF point >= 70 THEN
    SET credit = 'C';
  ELSEIF point >= 60 THEN
    SET credit = 'D';
  ELSE
    SET credit = 'F';
  END IF;
SELECT 
    CONCAT('  취득점수 =>  ',
            point,
            '  학점  =>  ',
            credit) AS '성적표';
END $$
DELIMITER ;

CALL ifProc_para(75);
CALL ifProc_para(90);
CALL ifProc_para(40);

-- ######################################
-- 스토어드 프로시저 테스트 -- CASE 

/*
CASE 
		WHEN 조건식1 THEN
			명령문1;
		WHEN 조건식2 THEN
			명령문2;
            
		ELSE
			명령문3;
END CASE;

*/
DROP PROCEDURE IF EXISTS case_test;
DELIMITER $$
CREATE PROCEDURE case_test(IN point INT)
BEGIN
  DECLARE credit CHAR(1);
  CASE 
	WHEN point >= 90 THEN
		SET credit = 'A';
	WHEN point >= 80 THEN
		SET credit = 'B';
	WHEN point >= 70 THEN
		SET credit = 'C';
	WHEN point >= 60 THEN
		SET credit = 'D';
	ELSE
		SET credit = 'F';
END CASE;
SELECT 
    CONCAT('  취득점수 =>  ', point,
            '  학점  =>  ', credit) AS '성적표';
END $$
DELIMITER ;

CALL case_test(75);
CALL case_test(90);
CALL case_test(40);


-- quiz (다중 if, case 명령문)
/*
CALL calPro(숫자1, 숫자2, 계산기호);

CALL calPro(10, 20, '+');
-- 10 + 20 = ?
*/

/*    다  중  I  F     */
DROP PROCEDURE IF EXISTS calPro;
DELIMITER $$
CREATE PROCEDURE calPro(IN num1 INT, num2 INT, gi VARCHAR(1))
BEGIN
  DECLARE result INT;
  IF gi = '+' THEN
    SET result = num1 + num2;
  ELSEIF gi = '-' THEN
    SET result = num1 - num2;
  ELSEIF gi = '*' THEN
    SET result = num1 * num2;
  ELSEIF gi = '/' THEN
	SET result = format(num1 / num2,2);  
  END IF;
  SELECT concat(num1, gi, num2, ' = ', result) AS '계산결과';
END $$
DELIMITER ;

CALL calPro(10, 20, '+');
CALL calPro(30, 20, '-');
CALL calPro(10, 20, '*');
CALL calPro(15, 3, '/');

/*     C  A  S  E     */
DROP PROCEDURE IF EXISTS calPro;
DELIMITER $$
CREATE PROCEDURE calPro(IN num1 INT, num2 INT, gi VARCHAR(1))
BEGIN
  DECLARE result INT;
  CASE
    WHEN gi = '+' THEN
      SET result = num1 + num2;
	WHEN gi = '-' THEN
      SET result = num1 - num2;
    WHEN gi = '*' THEN
      SET result = num1 * num2;
    WHEN gi = '/' THEN
      SET result = format(num1 / num2,2);  
  END CASE;
  SELECT concat(num1, gi, num2, ' = ', result) AS '계산결과';
END $$
DELIMITER ;

CALL calPro(10, 20, '+');
CALL calPro(30, 20, '-');
CALL calPro(10, 20, '*');
CALL calPro(15, 3, '/');


-- ######################################
-- 스토어드 프로시저 -- 반복문 

-- 반복문 WHILE
-- WHILE (조건식) DO
-- 		명령문
-- END WHILE;

-- ######################################

DROP PROCEDURE IF EXISTS whileProc1;
DELIMITER $$
CREATE PROCEDURE whileProc1()
BEGIN
  DECLARE i INT; -- 1에서 100까지 증가할 변수
  DECLARE sum INT; -- 더한 값을 누적할 변수
  SET i = 1;
  SET sum = 0;
  
  WHILE (i <= 100) DO
    SET sum = sum + i;
    SET i = i + 1;
  END WHILE;
  
  SELECT sum;
END $$
DELIMITER ;

CALL whileProc1();


/*
특정 회원의 정보를 출력하는 스토어드 프로시저
userTbl 테이블에서 조회
CALL info(이름) -> 레코드 출력
*/
SELECT * FROM userTbl;

DROP PROCEDURE IF EXISTS infoPrint;
DELIMITER $$
CREATE PROCEDURE infoPrint(IN userName VARCHAR(10))
BEGIN
  SELECT * FROM userTbl WHERE name = userName;
END $$
DELIMITER ;

CALL infoPrint('조관우');

use world;
show tables;
/*
world.country 테이블 활용
나라코드를 입력하면 GNP를 USD(달러)와 KRW(원)으로 출력하기
CALL gnpPrint('IND');
-> 출력형태
나라코드    나라이름    GNP(USD)    GNP(KRW)
환율 : $1 -> 1156원
*/
DESC country;
select * from country;

DROP PROCEDURE IF EXISTS gnpPrint;
DELIMITER $$
CREATE PROCEDURE gnpPrint(IN coName CHAR(3))
BEGIN  
  SELECT Code AS '나라코드', Name AS '나라이름', format(GNP, 0) AS 'GNP(USD)', format((GNP*1156), 0) AS 'GNP(KRW)' FROM country WHERE Code = coName;
END $$
DELIMITER ;

CALL gnpPrint('IND');
CALL gnpPrint('ESH');
CALL gnpPrint('MAR');

/*
quiz : employees.employees
나이대를 입력하면 그 나이대의 레코드를 출력하여라
CALL agePrint(50);
*/
use employees;
desc employees;
select * from employees;
select emp_no, (YEAR(NOW()) - YEAR(birth_date)) AS 'age' from employees where (YEAR(NOW()) - YEAR(birth_date)) BETWEEN 50 AND 59;

DROP PROCEDURE IF EXISTS agePrint;
DELIMITER $$
CREATE PROCEDURE agePrint(IN age INT)
BEGIN
  SELECT * from employees  where (YEAR(NOW()) - YEAR(birth_date)) BETWEEN age AND (age+9) ORDER BY age;
END $$
DELIMITER ;

CALL agePrint(50);
CALL agePrint(60);

show tables;
CREATE TABLE employees_test(SELECT * FROM employees);
SELECT * FROM employees_test;
ALTER TABLE employees_test
  ADD age INT
  DEFAULT (YEAR(NOW()) - YEAR(birth_date));

ALTER TABLE employees_test
DROP COLUMN age;

DROP PROCEDURE IF EXISTS agePrint2;
DELIMITER $$
CREATE PROCEDURE agePrint2(IN ageD INT)
BEGIN
  SELECT * from employees_test where age BETWEEN ageD AND (ageD+9) ORDER BY age;
END $$
DELIMITER ;

CALL agePrint2(50);
CALL agePrint2(60);

/*
employees, titles 테이블에서 조인해서 표시
직무(title)에 해당하는 총인원수와 이름 레코드 표시
CALL titleInfo('Staff');
출력포맷
총인원수 => ~명
이름1
이름2
...
*/
desc employees;
desc titles;
select * from employees;
select * from titles;

SELECT * FROM employees E
INNER JOIN titles T ON E.emp_no = T.emp_no;

SELECT E.emp_no, T.title, concat(first_name,' ', last_name) AS 'name' FROM employees E
  INNER JOIN titles T ON E.emp_no = T.emp_no
  WHERE title = 'Staff';
  
DROP PROCEDURE IF EXISTS titleInfo;
DELIMITER $$
CREATE PROCEDURE titleInfo(IN mytitle VARCHAR(10))
BEGIN
  SELECT concat(format(COUNT(*), 0), '명') AS '총인원수' FROM employees E
    INNER JOIN titles T ON E.emp_no = T.emp_no
  WHERE title = mytitle
    UNION
  SELECT concat(first_name, ' ', last_name) FROM employees E
    INNER JOIN titles T ON E.emp_no = T.emp_no
  WHERE title = mytitle;
END $$
DELIMITER ;

CALL titleInfo('Staff');
