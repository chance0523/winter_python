# 1/9 - [TABLE](#table) / [FILTERING](#filtering) / [SUBQUERY](#sub-query)
- ### TABLE
   - #### CREATE TABLE, INSERT RECORD
     + ##### CREATE TABLE
       ```mysql
       CREATE TABLE userTbl
       ( userID	CHAR(8) NOT NULL PRIMARY KEY,
         name          VARCHAR(10) NOT NULL,
         birthYear     INT NOT NULL,
         addr          CHAR(2) NOT NULL,
         mobile1       CHAR(3),
         mobile2       CHAR(8),
         height        SMALLINT,
         mDate         DATE
       );
       ```
     + ##### INSERT RECORD
       ```mysql
       INSERT INTO userTbl VALUES('LSG', '이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8');
       INSERT INTO userTbl VALUES('KBS', '김범수', 1979, '경남', '011', '2222222', 173, '2012-4-4');
       INSERT INTO userTbl VALUES('KKH', '김경호', 1971, '전남', '019', '3333333', 177, '2007-7-7');
       ```
- ### FILTERING
  - #### WHERE / BETWEEN / IN / LIKE
    + ##### WHERE
      ```MYSQL
      -- userTbl 테이블에서 birthYear가 1970보다 크거나 같고 height이 182보다 작다
      SELECT * FROM userTbl WHERE birthYear >= 1970 AND height < 182;
      ```
    + ##### BETWEEN
      ```MYSQL
      -- BETWEEN 값1 AND 값2 : 값1 ~ 값2
      SELECT userID, name FROM userTbl WHERE height BETWEEN 180 AND 183;
      ```
    + ##### IN
      ```MYSQL
      -- userTbl 에서 addr 컬럼값이 경남, 전남, 경북인 레코드 출력
      SELECT COUNT(*) FROM userTbl WHERE addr = '경남' OR addr = '전남' OR addr = '경북'; -- 4
      SELECT COUNT(*) FROM userTbl WHERE addr IN ('경남','전남','경북'); -- 4
      ```
    + ##### LIKE
      ```MYSQL
      SELECT COUNT(*) FROM userTbl WHERE name LIKE '김%'; -- 2
      SELECT COUNT(*) FROM userTbl WHERE name LIKE '김__'; -- 2
      SELECT COUNT(*) FROM userTbl WHERE name LIKE '김_'; -- 0   _ 의 갯수에 따라 달라짐
      SELECT * FROM userTbl WHERE name LIKE '_종신'; -- 윤종신
      ```
- ### SUB QUERY
  - #### SELECT .. FROM .. WHERE 조건절1 (SELECT .. FROM .. WHERE 조건절2)
    + ##### 주의 사항 : 서브쿼리의 레코드 결과값은 1개로 유일해야한다.
      ```MYSQL
      SELECT name, height FROM userTbl WHERE height > (SELECT height FROM userTbl WHERE name = '김경호');
      ```
    + ##### 서브쿼리의 레코드가 다중인 경우 : ANY (서브쿼리문)
      ```MYSQL
      SELECT name, height FROM userTbl WHERE height >= ANY (SELECT height FROM userTbl WHERE addr = '경남');
      ```
- ### ORDER BY / DISTINCT / GROUP BY / HAVING / WITH ROLLUP
  - #### ORDER BY
    + ##### ORDER BY 컬럼명 ASC/DESC
      ```MYSQL
      SELECT * FROM userTbl ORDER BY birthYear;
      SELECT * FROM userTbl ORDER BY birthYear DESC;
      ```
  - #### DISTINCT
    + ##### 레코드 값의 중복 제거
      ```MYSQL
      SELECT DISTINCT addr FROM userTbl;
      ```
  - #### GROUP BY
    + ##### SUM(), AVG()
      ```MYSQL
      SELECT SUM(price) AS '합계', AVG(price) AS '평균' FROM buyTbl;
      ```
    + ##### 그룹 이름별로 합계와 평균 구하기
      ```MYSQL
      SELECT groupName, SUM(price) AS '합계' , AVG(price) AS '평균' FROM buyTbl GROUP BY groupName ORDER BY groupName;
      ```
  - #### HAVING / WITH ROLLUP
    - ##### HAVING
      ```MYSQL
      -- buyTbl 에서 사용자별(GROUP BY) 총 구매액(price*amount)에서
      -- 조건 적용 : 총구매액이 1000보다 큰 레코드만 출력해라
      SELECT 
          userID AS '사용자 아이디',
          SUM(price * amount) AS '총구매액'
      FROM
          buyTbl
      GROUP BY userID
      HAVING SUM(price * amount) > 1000;
      ```
    - ##### WITH ROLLUP
      ```MYSQL
      SELECT groupName, SUM(price*amount) AS '비용' FROM buyTbl GROUP BY groupName WITH ROLLUP;
      ```
    