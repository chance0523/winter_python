-- #################################
-- 조인이란? p262
-- 두개이상의 테이블을 서로 묶어서 관리하는 기능 
-- 조인의 종류 
-- 내부 조인 
-- 외부 조인 
-- 크로스 조인 
-- 셀프 조인 

-- #################################
-- 예제 테이블 구조 확인 
-- 외래키 확인 
-- buytbl에서 외래키가 userID인지  확인 
-- 외래키는 Key값이 MUL로 표시 

USE sqldb;
DESC usertbl;
DESC buytbl;
-- FOREIGN KEY (userID) REFERENCES userTbl (userID)

/* ----------------------------------------- */
-- INNER JOIN 1 --
-- SELECT * 또는 컬럼명 
--    FROM 테이블1
--      INNER JOIN 테이블2
--         ON 조인될조건:테이블1.컬럼명 = 테이블2.컬럼명 이용 
-- 				(서로 공통된 관계의 컬럼이용)
--    [WHERE 조건절];
SELECT * FROM userTbl;
SELECT * FROM buyTbl;

-- buyTbl + userTbl 의 이너조인
-- 구매 경험이 있는 모든 레코드가 출력 
-- 구매 경험이 없는 레코드는 표시되지 않는다. => 아우터조인으로 해결 
-- userID 컬럼명이 2번 표시 
-- 왼쪽이 buyTbl, 오른쪽이 userTbl
SELECT
    *
FROM
    buyTbl
        INNER JOIN
    userTbl ON buyTbl.userID = userTbl.userID;

-- JYP 회원의 레코드 정보만 출력
SELECT 
    *
FROM
    buyTbl
        INNER JOIN
    userTbl ON buyTbl.userID = userTbl.userID
WHERE
    buyTbl.userID = 'JYP';

-- userID 가 두 번 출력 => 해결
-- userID / name / mobile1 / mobile2 
SELECT 
    buyTbl.userID, name, mobile1, mobile2 -- 테이블.userID 로 써야한다.
FROM
    buyTbl
        INNER JOIN
    userTbl ON buyTbl.userID = userTbl.userID
WHERE
    buyTbl.userID = 'JYP';

-- 별칭으로 명확하게 컬럼명 표시하기 
-- 테이블명.컬럼명으로 나열 
-- userID, prodName, amount, name, addr

SELECT 
    buyTbl.userID AS '아이디',
    buyTbl.prodName AS '상품명',
    buyTbl.amount AS '수량',
    userTbl.name AS '이름',
    userTbl.addr AS '지역'
FROM
    buyTbl
        INNER JOIN
    userTbl ON buyTbl.userID = userTbl.userID;

-- #################################
-- INNER JOIN 2 
-- 테이블명에 별칭 지정하기  
-- SELECT * 또는 별칭.컬럼명 
--    FROM 테이블1 테이블별칭1
--      INNER JOIN 테이블2 테이블별칭2
--         ON 조인될조건-별칭1.컬럼명 = 별칭2.컬럼명 이용 
-- 	 			(서로 공통된 관계의 컬럼이용)
--    [WHERE 조건절];

SELECT 
    B.userID AS '아이디',
    B.prodName AS '상품명',
    B.amount AS '수량',
    U.name AS '이름',
    U.addr AS '지역'
FROM
    buyTbl B
        INNER JOIN
    userTbl U ON B.userID = U.userID;


      
/* 퀴즈 
-- 아래와 같이 2개의 테이블(usertbl, buytbl)을 조인한 후  
-- 표시되게 만들어 보세요 

구매금액 = 수량*가격 

아이디  이름   지역   상품명   수량   가격   구매금액
  ?    ?      ?     ?      ?     ?       ?


-- 구매금액의 경우 
-- FORMAT(수식이나값, 소숫점자리수)
-- 3자리마다 콤마(,) 표시 
 */
SELECT 
    B.userID AS '아이디',
    U.name AS '이름',
    U.addr AS '지역',
    B.prodName AS '상품명',
    B.amount AS '수량',
    B.price AS '가격',
    FORMAT(B.amount * B.price, 0) AS '구매금액'
FROM
    buyTbl B
        INNER JOIN
    userTbl U ON B.userID = U.userID;

 
        
-- #################################        
-- 3개의 테이블 조인하기 p270
-- DB 접속과 3개의 테이블 생성 
-- 학생(stdTbl), 학생동아리(stdclubTbl), 동아리(clubTbl)
USE sqlDB;

-- 학생(stdTbl) 테이블 생성 - 이름, 지역 
CREATE TABLE stdTbl (
    stdName VARCHAR(10) NOT NULL PRIMARY KEY,
    addr CHAR(4) NOT NULL
);

DESC stdTbl;

CREATE TABLE clubTbl (
    clubName VARCHAR(10) NOT NULL PRIMARY KEY,
    roomNo CHAR(4) NOT NULL
);

DESC clubTbl;

CREATE TABLE stdclubTbl (
    num INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    stdName VARCHAR(10) NOT NULL,
    clubName VARCHAR(10) NOT NULL,
    FOREIGN KEY (stdName)
        REFERENCES stdTbl (stdName),
    FOREIGN KEY (clubName)
        REFERENCES clubTbl (clubName)
);
DESC stdclubTbl;


-- 데이타 입력 후 테이블 확인 
INSERT INTO stdTbl 
	VALUES 
		('김범수','경남'), ('성시경','서울'), ('조용필','경기'), 
        ('은지원','경북'),('바비킴','서울');
--         
INSERT INTO clubTbl 
	VALUES 
		('수영','101호'), ('바둑','102호'), 
		('축구','103호'), ('봉사','104호');
--     
INSERT INTO stdclubTbl 
	VALUES 
		(NULL, '김범수','바둑'), (NULL,'김범수','축구'), 
        (NULL,'조용필','축구'), (NULL,'은지원','축구'), 
        (NULL,'은지원','봉사'), (NULL,'바비킴','봉사');

SELECT * FROM stdTbl;
SELECT * FROM clubTbl;
SELECT * FROM stdclubTbl;

-- 3개의 테이블 조인하기1
-- 학생을 기준으로 학생이름, 지역, 가입 동아리, 동아리방번호 출력 
SELECT 
    S.stdName, S.addr, C.clubName, C.roomNo
FROM
    stdTbl S
        INNER JOIN
    stdclubTbl SC ON S.stdName = SC.stdName
        INNER JOIN
    clubTbl C ON SC.clubName = C.clubName
ORDER BY S.stdName; 

-- 3개의 테이블 조인하기2
-- 동아리를 기준으로 가입 동아리, 동아리방번호 , 학생이름, 지역 출력 

SELECT 
    C.clubName, C.roomNo, S.stdName, S.addr
FROM
    clubTbl C
        INNER JOIN
    stdclubTbl SC ON C.clubName = SC.clubName
        INNER JOIN
    stdTbl S ON SC.stdName = S.stdName
ORDER BY C.clubName;


-- #################################
-- 외부조인 (OUTER JOIN)
-- 조인의 조건에 만족되지 않는 행까지도 포함시킨다. 

-- SELECT * 또는 컬럼명 
--    FROM 테이블1
--      <LEFT/RIGHT/FULL> OUTER JOIN 테이블2
--         ON 조인될조건:테이블1.컬럼명 = 테이블2.컬럼명 이용 
-- 				(서로 공통된 관계의 컬럼이용)
--    [WHERE 조건절];


-- LEFT OUTER JOIN
-- 전체회원의 구매기록 확인하기.
-- 구매기록이 없는 회원도 모두 출력되어야 한다.
-- 왼쪽에 정의된 테이블 userTbl의 레코드가 모두 표시되어야한다. 

SELECT 
    *
FROM
    userTbl U
        LEFT OUTER JOIN
    buyTbl B ON U.userID = B.userID
ORDER BY U.userID;

-- RIGHT OUTER JOIN
        
SELECT 
    *
FROM
    userTbl U
        RIGHT OUTER JOIN
    buyTbl B ON U.userID = B.userID
ORDER BY U.userID;

-- 구매경험이 없는 회원 목록만 표시하여라 
-- WHERE .. IS NULL 
SELECT 
    *
FROM
    userTbl U
        LEFT OUTER JOIN
    buyTbl B ON U.userID = B.userID
WHERE B.userID IS NULL ORDER BY U.userID;

-- stdTbl, clubtbl, stdclubtbl 테이블에서 
-- 학생을 기준으로 동아리 학생 목록을 LEFT OUTER JOIN을 이용하여 출력하여라. 
-- 이때 동아리에 가입하지 않은 학생 목록도 출력한다.
SELECT 
    S.stdName, S.addr, C.clubName, C.roomNo
FROM
    stdTbl S
        LEFT OUTER JOIN
    stdclubTbl SC ON S.stdName = SC.stdName
        LEFT OUTER JOIN
    clubTbl C ON SC.clubName = C.clubName
ORDER BY S.stdName;

-- 동아리에 가입하지 않은 학생 목록을 출력하여라 
SELECT 
    S.stdName, S.addr, C.clubName, C.roomNo
FROM
    stdTbl S
        LEFT OUTER JOIN
    stdclubTbl SC ON S.stdName = SC.stdName
        LEFT OUTER JOIN
    clubTbl C ON SC.clubName = C.clubName
WHERE
    C.clubName IS NULL
ORDER BY S.stdName;  

-- stdTbl, clubtbl, stdclubtbl 테이블에서 
-- 동아리를 기준으로 가입한 학생 목록을 OUTER JOIN을 이용하여 출력하여라. 
-- 이때 가입학생이 아무도 없는 동아리 목록도 출력한다.
SELECT 
    C.clubName, C.roomNo,S.stdName,S.addr
FROM
    stdTbl S
        LEFT OUTER JOIN
    stdclubTbl SC ON S.stdName = SC.stdName
        RIGHT OUTER JOIN
    clubTbl C ON SC.clubName = C.clubName
ORDER BY C.clubName;  

-- 가입 학생이 없는 동아리명 목록을 출력하여라.     
SELECT 
    C.clubName, C.roomNo, S.stdName, S.addr
FROM
    stdTbl S
        LEFT OUTER JOIN
    stdclubTbl SC ON S.stdName = SC.stdName
        RIGHT OUTER JOIN
    clubTbl C ON SC.clubName = C.clubName
WHERE
    S.stdName IS NULL
ORDER BY C.clubName;  
    
-- stdTbl, clubtbl, stdclubtbl 테이블에서 
-- 학생을 기준으로 동아리 학생 목록을 OUTER JOIN을 이용하여 출력하여라. 
-- 이때 동아리에 가입하지 않은 학생 목록과 가입학생이 
--    없는 동아리 목록도 함께 출력한다.
-- UNION 활용. SELECT 문에 컬럼명이 같아야 한다. 
SELECT 
    S.stdName, S.addr, C.clubName, C.roomNo
FROM
    stdTbl S
        LEFT OUTER JOIN
    stdclubTbl SC ON S.stdName = SC.stdName
        LEFT OUTER JOIN
    clubTbl C ON SC.clubName = C.clubName 
UNION SELECT 
    S.stdName, S.addr, C.clubName, C.roomNo
FROM
    stdTbl S
        LEFT OUTER JOIN
    stdclubTbl SC ON S.stdName = SC.stdName
        RIGHT OUTER JOIN
    clubTbl C ON SC.clubName = C.clubName;
    
   
    