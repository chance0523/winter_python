-- SQL 퀴즈
USE employees;
SHOW TABLES;
SELECT * FROM employees LIMIT 10;
SELECT * FROM titles LIMIT 10;
SELECT * FROM salaries LIMIT 10;

-- 1. 직원 이름이 빠른 순(A, B, C …) 순으로 리스트를 출력하시오.
SELECT * FROM employees ORDER BY last_name, first_name;

-- 2. 직원 나이가 적은 순으로 출력하시오.
SELECT * FROM employees ORDER BY birth_date DESC;

-- 3. 직원 중 나이가 가장 많은 사람의 나이는 몇 살 인가?
-- employees 테이블에서 birth_date 필드에 MIN() 함수 적용
SELECT last_name, MIN(birth_date) FROM employees;
-- 연도만 출력하는 함수 적용 YEAR(날짜형 데이터) => 연도만 출력
SELECT YEAR(MIN(birth_date)) FROM employees; -- 1952
-- now() : 
-- curdate() : 
SELECT now(), curdate(); -- 2020-01-09 16:53:49 | 2020-01-09
SELECT YEAR(curdate());
SELECT YEAR(curdate())-YEAR(MIN(birth_date)) AS '최연장자의 나이' FROM employees;

-- 4. 직원들의 업무(titles)에는 직원별로 업무가 저장되어 있다. 이 회사의 업무 종류 리스트를 구하시오.
SELECT * FROM titles;
SELECT DISTINCT title FROM titles;

-- 5. 이 회사의 업무 종류 개수를 구하시오.
SELECT COUNT(DISTINCT title) AS '업무 종류 개수' FROM titles;

-- 6. 가장 최근에 입사한 사람 100명만 출력하시오
SELECT * FROM employees;
SELECT * FROM employees ORDER BY hire_date DESC LIMIT 100;


-- 7. 급여가 가장 많은 사람 10명을 구하시오.
SELECT * FROM salaries;
SELECT * FROM salaries ORDER BY salary DESC LIMIT 10;

-- 8. 급여가 가장 많은 사람 10명을 제외하고 다음 10명을 구하시오.
--   즉, 11등부터 20등 까지…
SELECT * FROM salaries ORDER BY salary DESC LIMIT 10,10;

-- 9. 입사한지 가장 오래된 사람의 이름은 무엇인가?
SELECT * FROM employees;
SELECT MIN(hire_date) FROM employees;
SELECT first_name, last_name, hire_date FROM employees
       WHERE hire_date = (SELECT MIN(hire_date) FROM employees);

-- 10. 1999년에 입사한 직원 리스트를 구하시오.
SELECT * FROM employees WHERE hire_date =
ANY (SELECT hire_date FROM employees WHERE YEAR(hire_date) = 1999);

-- 11. 1999년에 입사한 직원 중 여자 직원(GENDER='F') 리스트를 구하시오.
SELECT * FROM employees WHERE hire_date =
ANY (SELECT hire_date FROM employees WHERE YEAR(hire_date) = 1999);





-- 12. 1998년에 입사한 직원 중 남자 직원(M)은 몇 명인가?



-- 13. 1998년이나 1999년에 입사한 직원의 수를 구하시오.
SELECT COUNT(*) AS ' 1998년이나 1999년에 입사한 직원의 수'
FROM employees WHERE YEAR(hire_date)=1998 OR YEAR(hire_date)=1999;


-- 14. 1995년부터 1999년까지 입사한 직원의 수를 구하시오.
SELECT COUNT(*) AS ' 1995년~1999년에 입사한 직원의 수'
FROM employees WHERE YEAR(hire_date) BETWEEN 1995 AND 1999;


-- 15. 성(last_name)이 Senzako, Pettis, Henseler인 직원을 출력하시오.
SELECT * FROM employees WHERE last_name IN ('Senzako','Pettis','Henseler');

-- 16. EMPLOYEES 테이블을 복사하여 EMPLOYEES2 테이블을 만들어라
CREATE TABLE employees2 (SELECT * FROM employees);
SELECT * FROM employees2;

-- 17. EMPLOYEES2 테이블에서 구조만 그대로 두고 모든 레코드를 삭제하여라 
TRUNCATE TABLE employees2;
SELECT * FROM employees2;

-- 18. EMPLOYEES 테이블에서 성별이 남자인 레코드를 EMPLOYEES2 테이블로 
--       삽입하여라.
SELECT * FROM employees;
INSERT INTO employees2 (emp_no,birth_date, first_name, last_name, gender, hire_date)
       (SELECT emp_no,birth_date, first_name, last_name, gender, hire_date FROM employees WHERE gender = 'M');
SELECT * FROM employees2;

-- 19. EMPLOYEES2 테이블을 삭제하여라 
DROP TABLE employees2;
SHOW TABLES;

-- 20. employees2 DB를 생성하고 employees 데이타베이스에서 2개의 테이블을 복사하여라 
CREATE DATABASE employees2;
SHOW DATABASES;
USE employees2;
CREATE TABLE employees1 (SELECT * FROM employees.employees);
CREATE TABLE titles1 (SELECT * FROM employees.titles);
SHOW TABLES;
