USE world;
SELECT * FROM worldcity;
SELECT * FROM city;
DESC city;
SELECT * FROM gnpcountry;
DESC gnpcountry;
SELECT * FROM country;
DESC country;
SELECT * FROM countrylangcityuage;



-- 1. city 테이블에서 인구가 1500000 넘는 레코드만 다음과 같이 출력하시요.

/*
 나라       인구   
  ?   ***  ?    명
  ?   ***  ?    명 
 
 */
SELECT * FROM city;
SELECT 
    Name AS '나라',
    '***' AS ' ',
    Population AS '인구',
    '명' AS ' '
FROM
    city
WHERE
    Population > 1500000;
        
        
-- 2. gnpcountry 테이블에서 gnp가 가장 큰 레코드를 3위까지 출력하여라. 
-- 이때 gnp는 정수형으로 표시한다. 
/*
나라이름      GNP
  ?          ?
  ?          ?
  ?          ?
*/
SELECT * FROM gnpcountry;
SELECT 
    name AS '나라이름', CAST(gnp AS SIGNED INTEGER) AS 'GNP'
FROM
    gnpcountry
ORDER BY gnp DESC
LIMIT 3;



-- 3. country 테이블에서 독립년도(IndepYear)가 음수로 표시된 레코드만 양수로 출력하여라.
/*
  국가      독립년도
  ?          ?
  ?          ?
  ?          ?
*/
SELECT * FROM country;
SELECT 
    Name AS '국가', ABS(IndepYear) AS '독립년도'
FROM
    country
WHERE
    IndepYear < 0;

-- 4. country 테이블에서 독립년도(IndepYear)가 NULL인 경우 '알수없음' 으로 표시하여라. 

/*
  국가      독립년도
  ?        알수없음'
  ?          ?
  ?          ?
*/
SELECT * FROM country;
SELECT 
    Name AS '국가',
    IFNULL(IndepYear, '알수없음') AS '독립년도'
FROM
    country;

    
    
-- 5. countrylanguage 테이블에서 CountryCode 필드가 'M'으로 시작하는 레코드에서 
-- IsOfficial 필드가 'T' 이면 '공식언어', 'F'이면 '비공식언어'로 출력하여라 

/*
  CountryCode      Language     IsOfficial
	?        		?			  비공식언어
	?          		?              공식언어
*/
SELECT * FROM countrylanguage;
SELECT 
    CountryCode,
    Language,
    CASE IsOfficial
        WHEN 'T' THEN '비공식언어'
        WHEN 'F' THEN '공식언어'
        ELSE 'NULL'
    END AS 'IsOfficial'
FROM
    countrylanguage
WHERE
    CountryCode LIKE 'M%';
        
        
-- 6. country 테이블에서 독립년도(IndepYear)가 음수로 표시된 레코드의 필드값을 'BC' 와 함께 연도를 표시하여라 

/*
  국가         독립년도
  China     BC.1523
    ?            ?
    ?            ?
*/
SELECT * FROM country;
SELECT 
    Name AS '국가',
    REPLACE(IndepYear, '-', 'BC.') AS '독립년도'
FROM
    country
WHERE
    IndepYear < 0;

-- 7. country 테이블의 평균수명(LifeExpectancy)이 80이 넘는 레코드에서  평균수명(LifeExpectancy)의 레코드값을 소숫점 없이 표시하여라. 
-- 정렬은 평균수명(LifeExpectancy)을 기준으로 역정렬하며  출력포맷은 아래를 참조한다.

/*
  국가           평균수명
  Andorra        84 세
  Macao          82 세
    ?            ?
*/
SELECT * FROM country;
SELECT 
    Name AS '국가',
    CONCAT(FORMAT(LifeExpectancy, 0), ' 세') AS '평균수명'
FROM
    country
WHERE
    LifeExpectancy > 80
ORDER BY LifeExpectancy DESC;



    

-- 8. country 테이블에서 GovernmentForm이 'Overseas Department of France'인 레코드를 출력한 후 
-- 'Overseas Department of France' 필드값을 문자열함수를 이용하여  ' *** France'로 교체하여라 
/*
      국가              지역            정부
  Guadeloupe        Caribbean    *** France
      ?                ?              ?
*/
SELECT * FROM country;
SELECT 
    Name AS '국가',
    Region AS '지역',
    REPLACE(GovernmentForm,
        'Overseas Department of',
        '***') AS '정부'
FROM
    country
WHERE
    GovernmentForm = 'Overseas Department of France';





--  9. worldcity 테이블에서 문자열함수와 format()을 이용하여 아래와 같은 형태로 출력하여라. 
-- 2개의 필드로 구성되어 있으며 국가 필드의 경우  code와 name 필드를 함께 표시되도록 한다.
/*
      국가               			GNP
  (USA)/ United States      8,510,700
         ?                      ?           
*/
SELECT * FROM worldcity;
SELECT 
    CONCAT('(', Code, ') / ', Name) AS '국가',
    FORMAT(GNP, 0) AS 'GNP'
FROM
    worldcity;



-- 10. 날짜 함수와 문자열 함수를 이용하여 오늘 날짜를 기준으로 다음과 같이 출력하여라 

/*
오늘은 2020년 1월 10일 토요일입니다.
*/
SELECT 
    '오늘은',
    YEAR(NOW()) AS '년',
    '년',
    MONTH(NOW()) AS '월',
    '월',
    DAY(NOW()) AS '일',
    '일',
    CASE DAYOFWEEK(NOW())
        WHEN 1 THEN '일요일'
        WHEN 2 THEN '월요일'
        WHEN 3 THEN '화요일'
        WHEN 4 THEN '수요일'
        WHEN 5 THEN '목요일'
        WHEN 6 THEN '금요일'
        ELSE '토요일'
    END AS '요일',
    '입니다.';
    


-- 11. 날짜함수를 이용하여 아래와 같이 오늘 날짜를 기준으로 출력하여라 
-- 수료식 날짜는 2020년 2월 18일로 한다. 

/* 수료식 앞으로 ?  39일 */
SELECT 
    '수료식 앞으로 ? ',
    DATEDIFF('2020-2-18', NOW()) AS '수료식까지 남은 날',
    '일';



