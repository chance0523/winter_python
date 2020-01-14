# 1/14 - [IF](#if) / [CASE](#case)
- ### IF / CASE
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