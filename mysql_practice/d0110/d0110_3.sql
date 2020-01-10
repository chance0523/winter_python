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


  

-- ###################################
-- 셀프 조인(자체 조인) 
-- p278
-- INNER JOIN의 일종. 같은 테이블을 조인한다. 
-- 조직도등에 이용  

-- 테이블 생성 p280  
-- sqlDB 안에 empTBL 테이블 생성 
-- sqlDB/empTBL 

-- 테이블 데이타 
-- INSERT INTO empTbl VALUES('나사장',NULL,'0000');
-- INSERT INTO empTbl VALUES('김재무','나사장','2222');
-- INSERT INTO empTbl VALUES('김부장','김재무','2222-1');
-- INSERT INTO empTbl VALUES('이부장','김재무','2222-2');
-- INSERT INTO empTbl VALUES('우대리','이부장','2222-2-1');
-- INSERT INTO empTbl VALUES('지사원','이부장','2222-2-2');
-- INSERT INTO empTbl VALUES('이영업','나사장','1111');
-- INSERT INTO empTbl VALUES('한과장','이영업','1111-1');
-- INSERT INTO empTbl VALUES('최정보','나사장','3333');
-- INSERT INTO empTbl VALUES('윤차장','최정보','3333-1');
-- INSERT INTO empTbl VALUES('이주임','윤차장','3333-1-1');


-- 직원의 상관의 구내번호를 찾아라 
-- 직원(emp), 상관(manager), 구내번호(empTel) 
-- 가로로 2번 컬럼이 반복되어 표시 


-- 우대리 직원의 상관의 구내번호를 찾아라 




-- ###################################
-- UNION / UNION ALL (p281)
-- 쿼리의 결과를 합쳐서 보여준다. 
-- UNION 중복 허용 
-- UNION ALL 중복된 부분 삭제 

-- SELECT ... -- 쿼리1
-- UNION
-- SELECT ... -- 쿼리2




-- NOT IN : 첫번째 쿼리의 결과중 두번째 쿼리에 해당하는 것을 제외 
-- IN : 두번째 쿼리의 결과만 조회 

-- SELECT 첫번째 쿼리 
-- 		WHERE ... [NOT IN / IN ] ( SELECT 두번째 쿼리 )

-- SELECT * 또는 컬럼명 FROM 테이블1
--    WHERE 조건절1 NOT IN 또는 IN ( SELECT * 또는 컬럼명 FROM 테이블2 WHERE 조건절2) ;

-- 사용자중 전화가 없는 사람을 제외하고 싶다. NOT IN
-- 사용자중 전화가 없는 사람만 조회 IN





