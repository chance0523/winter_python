USE sqldb;
-- 변수 생성과 출력 p.234
-- SET @변수명 = 초기값; -- 변수의 선언 및 값 대입
-- SELECT @변수명 -- 변수의 값 출력

SET @a = 1;
SET @b = 10;
SET @c = 'MySQL';
SET @d = 'sqLite';

SELECT @a, @b, @c, @d;
SELECT @a, @b, @a + @b, @a * @b;
SELECT @c, @d, @c + @d; -- 'MySQL', 'sqLite', '0'

-- 테이블과 변수 함께 사용하기
SELECT * FROM userTbl;

SET @deco = '***';
SELECT @deco;
SELECT 
    userID AS '아이디', @deco AS ' ', addr AS '지역'
FROM
    userTbl;
    
-- userTbl에서 키가 180이 넘는 레코드만 추출한 후 아래와 같은 형태로 출력하여라
SET @irm = '가수이름 =>';
SET @cm = 'cm';
SELECT @irm;
SELECT 
    @irm AS ' ', name AS '이름', height AS '키', @cm AS ' '
FROM
    userTbl
WHERE
    height > 180;

