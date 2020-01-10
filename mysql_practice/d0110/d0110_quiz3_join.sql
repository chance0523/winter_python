use employees;

SELECT * from employees limit 5;
SELECT * from dept_emp limit 5;
SELECT * from titles limit 5;

-- 1. 현재 근무 중인 직원 정보를 출력하시오.
-- 현재 근무 중은? to_date='9999-01-01'
-- Step1 : employees 테이블과 dept_emp 테이블 조인 
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가 
/*
사원번호  이름   성   성별   입사일(hire_date)  현재 근무중 
  ?      ?    ?    ?           ?          9999-01-01 
*/
SELECT 
    E.emp_no AS '사원번호',
    E.first_name AS '이름',
    E.last_name AS '성',
    E.gender AS '성별',
    E.hire_date AS '입사일(hire_date)',
    D.to_date AS '현재 근무중'
FROM
    employees E
        INNER JOIN
    dept_emp D ON E.emp_no = D.emp_no
WHERE
    D.to_date = '9999-01-01'
;

 
 
-- 2. 현재 근무 중인 직원의 모든 정보(수행업무 포함) 를 출력하시오.
-- 현재 근무 중은? to_date='9999-01-01'
-- Step1 : employees 테이블과 title 테이블 조인 
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가 
/*
사원번호  이름   성   직무(title)  현재 근무중 
  ?      ?    ?        ?     9999-01-01 
*/
SELECT * from employees limit 5;
SELECT * from titles limit 5;
SELECT 
    E.emp_no AS '사원번호',
    E.first_name AS '이름',
    E.last_name AS '성',
    T.title AS '직무(title)',
    T.to_date AS '현재 근무중'
FROM
    employees E
        INNER JOIN
    titles T ON E.emp_no = T.emp_no
WHERE
    T.to_date = '9999-01-01'
;

-- 3. 현재 근무 중인 부서명를 출력하시오. (사원번호, 사원명, 부서코드, 부서명)
-- 3개의 테이블 조인 
-- Step1 : dept_emp , employees, departments 테이블에서 
-- Step2 : 1의 조인 명령 마지막에 WHERE 조건절 추가 
/*
사원번호  사원명  부서코드(dept_no)  부서명(dept_name)  현재 근무중 
  ?      ?        ?               ?             9999-01-01 

*/

SELECT * from employees limit 5;
SELECT * from dept_emp limit 5;
SELECT * from departments limit 5;
SELECT 
    E.emp_no AS '사원번호',
    CONCAT(E.first_name, ' ', E.last_name) AS '사원명',
    DE.dept_no AS '부서코드(dept_no)',
    D.dept_name AS '부서명(dept_name)',
    DE.to_date AS '현재 근무중'
FROM
    employees E
        INNER JOIN
    dept_emp DE ON E.emp_no = DE.emp_no
        INNER JOIN
    departments D ON DE.dept_no = D.dept_no
WHERE
    DE.to_date;

