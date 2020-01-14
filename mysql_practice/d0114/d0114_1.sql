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
