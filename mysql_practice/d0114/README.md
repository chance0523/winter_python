# 1/14 - [IF](#if) / [CASE](#case) / [WHILE](#while) / [CONNECT](#connect)
- ### IF / CASE / WHILE
  - #### IF
    - ##### IF
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
    - ##### 다중 IF
      ```MYSQL
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
          CONCAT('  취득점수 =>  ', point,
                  '  학점  =>  ', credit) AS '성적표';
      END $$
      DELIMITER ;

      CALL ifProc_para(75);
      CALL ifProc_para(90);
      CALL ifProc_para(88);
      ```
    - #### CASE
      + ##### USE CASE WITH STORED PROCEDURE
        ```mysql
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
        ```
    - #### WHILE
      - ##### WHILE
        ```MYSQL
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
        ```
- ### CONNECT
  - #### CONNECT TO DATABSE
    + ##### CONNECT
      ```python
      import pymysql

      conn = pymysql.connect(host='localhost',
                             port=3306, user='root',
                             passwd='1234', db='world', charset='utf8')
      ```
    + ##### CREATE CURSOR
      ```python
      cursor = conn.cursor()
      cursor.execute(
          'SELECT * FROM city;'
      )
      cityList = cursor.fetchall()
      print(cityList)
      ```
    + ##### CREATE DICTIONARY CURSOR
      ```python
      cursor = conn.cursor(pymysql.cursors.DictCursor)
      ```