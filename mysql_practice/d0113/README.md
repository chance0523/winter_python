# 1/13 - [JOIN](#join) / [UNION](#union) / [TABLE](#table) / [VIEW](#view) / [STORED PROCEDURE](#stored-procedure)
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
  - #### ADD / CHANGE / DROP FIELD
    + ##### ADD FIELD
      ```mysql
      -- userTbl_aa 에 homePage(VARCHAR(30)) 필드 추가하기
      ALTER TABLE userTbl_aa
      ADD homePage VARCHAR(30)
      DEFAULT 'http://google.com'
      NULL;
      ```
    + ##### CHANGE FIELD
      ```mysql
      -- userTbl_aa의 age 필드명을 userAge로 변경
      ALTER TABLE userTbl_aa
      CHANGE COLUMN age userAge INT(3);
      ```
    + ##### DROP FILED
      ```mysql
      -- userTbl_aa의 height 필드를 삭제
      ALTER TABLE userTbl_aa
      DROP COLUMN height;
      ```
  - #### ADD / DROP PRIMARY KEY
    + ##### ADD PRIMARY KEY
      ```MYSQL
      -- userTbl_aa 테이블에서 userID를 기본키로 설정하기
      ALTER TABLE userTbl_aa
        ADD CONSTRAINT PK_userTbl_aa_userID
        PRIMARY KEY(userID);
      ```
    + ##### DROP PRIMARY KEY
      ```MYSQL
      ALTER TABLE userTbl_aa
        DROP PRIMARY KEY;
      ```
  - #### ADD / DROP FOREIGN KEY
    + ##### ADD FOREIGN KEY
      ```mysql
      ALTER TABLE buyTbl_aa
        ADD CONSTRAINT FK_userTbl_aa_buyTbl_aa
        FOREIGN KEY (userID)
        REFERENCES userTbl_aa(userID);
      ```
    + ##### DROP FOREIGN KEY
      ```mysql
      ALTER TABLE buyTbl_aa
        DROP FOREIGN KEY FK_userTbl_aa_buyTbl_aa;
      ```
 - ### VIEW
   - #### CREATE / DROP VIEW
     + ##### CREATE VIEW
       ```mysql
       -- userTbl 테이블에서 id, name, addr => v_userTbl 뷰 생성
       CREATE VIEW v_userTbl AS
       SELECT userID, name, addr FROM userTbl;
       ```
     + ##### DROP VIEW
       ```mysql
       DROP VIEW v_userTbl;
       ```
     + ##### INSERT VIEW
       ```mysql
       INSERT INTO v_userTbl VALUES ('ASS','안성수',2009,'부산');
       -- view와 원본 table 둘 다에 삽입된다.
       ```
     + ##### UPDATE VIEW
       ```MYSQL
       UPDATE v_userTbl SET addr = '서울';
       -- view와 원본 table 둘 다 수정된다.
       ```
     + ##### DELETE RECORD
       ```MYSQL
       DELETE FROM v_userTbl WHERE name = '안성수';
       -- view와 원본 table의 레코드 둘 다 삭제된다.
       ```
- ### STORED PROCEDURE
  - #### CREATE / CALL STORED PROCEDURE
    - ##### CREATE STORED PROCEDURE
      ```MYSQL
      DELIMITER $$
      CREATE PROCEDURE varTest()
      BEGIN
        SELECT 'hello MySQL';
      END $$
      DELIMITER ;
      ```
    - ##### CALL STORED PROCEDURE
      ```MYSQL
      CALL varTest();
      ```
  - #### STORED PROCEDURE WITH PARAMETERS
    + ##### Calculator Procedure
      ```mysql
      -- calculator procedure
      DELIMITER $$
      CREATE PROCEDURE calPro(IN num1 INT(3), num2 INT(3))
      BEGIN
      SELECT num1, num2,
      concat(num1+num2) AS '+' ,concat(num1-num2) AS '-',
      concat(num1*num2) AS '*', format(concat(num1/num2),2) AS '/';
      END $$
      DELIMITER ;

      CALL calPro(10, 5)
      ```
  - #### IF
    - ##### USE IF WITH PROCEDURE
      ```MYSQL
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
      ```
