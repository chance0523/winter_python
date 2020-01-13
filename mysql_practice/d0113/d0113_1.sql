-- ###################################
-- 크로스 조인 (상호조인) 
-- p277
-- 키가 정의되어 있지 않아도 된다. 
-- 모든행이 반복됨 
-- 한쪽 테이블의 모든 행과 다른쪽 테이블의 모든 행이 조인됨 => 카티션곱
-- SELECT * 또는 컬럼명
--    FROM 테이블1 
--      CROSS JOIN 테이블2;

-- buyTbl, userTbl 테이블에서 CROSS JOIN을 적용하여라. 

SHOW DATABASES;
USE SQLDB;
SHOW TABLES;

SELECT * FROM buyTbl;
SELECT COUNT(*) FROM buyTbl;  -- 14
SELECT * FROM userTbl;
SELECT COUNT(*) FROM userTbl;  -- 10
SELECT * FROM buyTbl CROSS JOIN userTbl;
SELECT COUNT(*) FROM buyTbl CROSS JOIN userTbl;  -- 140


-- ###################################
-- 셀프 조인(자체 조인) 
-- p278
-- INNER JOIN의 일종. 같은 테이블을 조인한다. 
-- 조직도등에 이용  

-- 테이블 생성 p280  
-- sqlDB 안에 empTBL 테이블 생성 
-- sqlDB/empTBL 
CREATE TABLE empTbl (
    emp CHAR(3),
    manager CHAR(3),
    empTel VARCHAR(8)
);

-- 테이블 데이타 
INSERT INTO empTbl VALUES('나사장',NULL,'0000');
INSERT INTO empTbl VALUES('김재무','나사장','2222');
INSERT INTO empTbl VALUES('김부장','김재무','2222-1');
INSERT INTO empTbl VALUES('이부장','김재무','2222-2');
INSERT INTO empTbl VALUES('우대리','이부장','2222-2-1');
INSERT INTO empTbl VALUES('지사원','이부장','2222-2-2');
INSERT INTO empTbl VALUES('이영업','나사장','1111');
INSERT INTO empTbl VALUES('한과장','이영업','1111-1');
INSERT INTO empTbl VALUES('최정보','나사장','3333');
INSERT INTO empTbl VALUES('윤차장','최정보','3333-1');
INSERT INTO empTbl VALUES('이주임','윤차장','3333-1-1');

select * from empTbl;
-- 직원의 상관의 구내번호를 찾아라 
-- 직원(emp), 상관(manager), 구내번호(empTel) 
-- 가로로 2번 컬럼이 반복되어 표시 


-- 우대리 직원의 상관의 구내번호를 찾아라 
SELECT 
    a.EMP AS '부하직원',
    b.EMP AS '직속상관',
    B.empTel AS '직속상관연락처'
FROM
    empTbl A
        INNER JOIN
    empTbl B ON A.manager = B.emp
WHERE
    A.emp = '우대리';



-- ###################################
-- UNION / UNION ALL (p281)
-- 쿼리의 결과를 합쳐서 보여준다. 
-- UNION 중복 허용 
-- UNION ALL 중복된 부분 삭제 
-- 쿼리1의 결과 필드수와 쿼리2의 결과 필드수가 같아야 한다.

-- SELECT ... -- 쿼리1
-- UNION
-- SELECT ... -- 쿼리2

SHOW TABLES;
SELECT * FROM clubTbl;
SELECT * FROM stdTbl;
SELECT stdName, addr FROM stdTbl
	UNION ALL
SELECT clubName, roomNO FROM clubTbl;

-- NOT IN : 첫번째 쿼리의 결과중 두번째 쿼리에 해당하는 것을 제외 
-- IN : 두번째 쿼리의 결과만 조회 

-- SELECT 첫번째 쿼리 
-- 		WHERE ... [NOT IN / IN ] ( SELECT 두번째 쿼리 )

-- SELECT * 또는 컬럼명 FROM 테이블1
--    WHERE 조건절1 NOT IN 또는 IN ( SELECT * 또는 컬럼명 FROM 테이블2 WHERE 조건절2) ;

-- 사용자중 전화가 없는 사람을 제외하고 싶다. NOT IN
-- 사용자중 전화가 없는 사람만 조회 IN

SELECT name, CONCAT(mobile1,mobile2) AS '전화번호' FROM userTbl
WHERE name NOT IN (SELECT name FROM userTbl WHERE mobile1 IS NULL);

SELECT name, CONCAT(mobile1,mobile2) AS '전화번호' FROM userTbl
WHERE name IN (SELECT name FROM userTbl WHERE mobile1 IS NULL);

-- quiz
-- employees 데이터베이스의 employees, dept_emp 테이블을
-- UNION 명령으로 아래 조건의 레코드만 출력하여라
-- 현재근무중(to_date = 9999~), emp_no >= 499995
-- 성별은 남자(M), 입사일(hire_date)가 1999년 9월 이후
-- 이름이 C로 시작
/*
사원번호+이름        근무중+입사일
*/

use employees;
show tables;
select * from employees;
select * from dept_emp;
SELECT 
    emp_no, first_name
FROM
    employees
WHERE
    emp_no >= 499995 AND gender = 'M'
    UNION SELECT from_date, to_date FROM dept_emp;
    

use employees;
select * from employees where gender = 'M' or year(hire_date)>1995;

SELECT 
    *
FROM
    employees
WHERE
    ((YEAR(hire_date) = 1999)
        AND (MONTH(hire_date) >= 9))
        OR (YEAR(hire_date) > 1999);
