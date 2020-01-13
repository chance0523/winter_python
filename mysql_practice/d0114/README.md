# 1/14 - [JOIN](#join) /
- ### JOIN
   - #### CROSS JOIN / SELF JOIN
     + ##### CROSS JOIN
       ##### 한쪽 테이블의 모든 행과 다른쪽 테이블의 모든 행이 조인됨 => 카티션곱
       ```mysql
       SELECT * FROM buyTbl CROSS JOIN userTbl;
       ```
     + ##### SELF JOIN
       ##### 별도의 구문이 있는 것이 아니라 자기 자신과 자기 자신이 조인 (조직도에 사용)
       ```mysql
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
       ```
