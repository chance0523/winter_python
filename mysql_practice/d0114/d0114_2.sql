-- 컬럼의 값 일괄로 변경하기
DESC employees.employees;
-- gender = M/F
-- sqldb/employeesTb
USE sqldb;
DROP TABLE employeesTb;
CREATE TABLE employeesTb (SELECT * FROM employees.employees LIMIT 20);
SELECT * FROM employeesTb;

-- 특정 레코드의 gender 값 변경하기 (M => Male , F => Female)
DROP PROCEDURE IF EXISTS genderChange1;
DELIMITER $$
CREATE PROCEDURE genderChange1(IN num INT(3))
BEGIN
  SELECT @result:= gender AS 'gender' FROM employeesTb
    WHERE emp_no = num;
    
  IF @result = 'M' THEN
    UPDATE employeesTb SET gender = 'Male';
  ELSE  -- F
    UPDATE employeesTb SET gender = 'Female';
  END IF;
END $$
DELIMITER ;

DESC employeesTb;
ALTER TABLE employeesTb
  MODIFY gender CHAR(10);
  
CALL genderChange1(10004);	
SELECT * FROM employeesTb;

CREATE TABLE employeesTb2 (SELECT * FROM employees.employees LIMIT 20);
SELECT * FROM employeesTb2;
DESC employeesTb2;

-- employeesTb2의 gender 모든 값 변경
SELECT COUNT(*) FROM employeesTb2;

ALTER TABLE employeesTb2
  MODIFY gender CHAR(10);
  
DROP PROCEDURE IF EXISTS genderChange2;
DELIMITER $$
CREATE PROCEDURE genderChange2()
BEGIN
  DECLARE i INT;
  SET i = 1;
  -- 전체 레코드 수
  SELECT @tot := COUNT(*) FROM employeesTb2;
  -- 전체 레코드수만큼 명령 실행
  WHILE (i <= @tot) DO
    
    SET i = i + 1;
  END WHILE;
END $$
DELIMITER ;

CALL genderChange2();
