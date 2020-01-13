# 1/13 - [join](#join) / [union](#union) / [table](#table)
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
- ### UNION
   - #### UNION / UNION ALL
     + ##### 쿼리의 결과를 합쳐서 보여줌. 쿼리1의 결과 필드수와 쿼리2의 결과 필드수가 같아야 한다.
       ##### UNION은 중복 허용 / UNION ALL은 중복된 부분 삭제
       ```MYSQL
       SELECT stdName, addr FROM stdTbl
         UNION ALL
       SELECT clubName, roomNO FROM clubTbl;
       ```
   - #### NOT IN / IN
     + ##### NOT IN : 첫번째 쿼리의 결과중 두번째 쿼리에 해당하는 것을 제외
       ```mysql
       -- 사용자중 전화가 없는 사람을 제외하고 싶다.
       SELECT name, CONCAT(mobile1,mobile2) AS '전화번호' FROM userTbl
          WHERE name NOT IN (SELECT name FROM userTbl WHERE mobile1 IS NULL);
       ```
     + ##### IN : 두번째 쿼리의 결과만 조회
       ```mysql
       -- 사용자중 전화가 없는 사람만 조회하고 싶다.
       SELECT name, CONCAT(mobile1,mobile2) AS '전화번호' FROM userTbl
          WHERE name IN (SELECT name FROM userTbl WHERE mobile1 IS NULL);
       ```

- ### TABLE
  - #### ADD / CHANGE FIELD
    + ##### ADD
      ```mysql
      -- userTbl_aa 에 homePage(VARCHAR(30)) 필드 추가하기
      ALTER TABLE userTbl_aa
      ADD homePage VARCHAR(30)
      DEFAULT 'http://google.com'
      NULL;
      ```
    + ##### CHANGE
      ```mysql
      -- userTbl_aa의 age 필드명을 userAge로 변경
      ALTER TABLE userTbl_aa
      CHANGE COLUMN age userAge INT(3);
      ```