# 1/10 - variable / control flow function
- ### variable
  - #### create variable
    + ##### SET @variable_name;
      ```mysql
      SET @a = 1;
      SET @b = 'MySQL';
      ```
   - #### (cast / convert) variable type
     + CAST ( ... AS variable type)
        ```mysql
        -- 실수 => 정수
        SELECT
            CAST(AVG(amount) AS SIGNED INTEGER) AS '평균 구매 갯수'
        FROM buyTbl;
        ```
     + CONVERT ( ... , variable type)
       ```mysql
       -- 숫자가 포함된 문자열
       SELECT CONVERT('2nd', SIGNED INTEGER); -- 2
       SELECT CONVERT('2nd123', SIGNED INTEGER); -- 2
       ```
   
  - #### 제어 흐름 함수 (control flow function)
    + ##### IF(수식, True 값1, False 값2)
      ```mysql
      SELECT IF(100 < 200, '크다', '작다'); -- 크다
      SELECT IF(100 > 200, '크다', '작다'); -- 작다
      ```
    + ##### IFNULL(수식1, 수식2) : 수식1이 NULL이 아니면 수식1 반환, NULL 이면 수식2 반환
      ```mysql
      SELECT IFNULL(NULL, 'NULL값이다'); -- NULL값이다
      SELECT IFNULL(100 + 300, 'NULL값이다.'); -- 400
      ```
    + ##### NULLIF(수식1, 수식2) : 수식1과 수식2가 같으면 NULL, 다르면 수식1 반환
      ```mysql
      SELECT NULLIF(50 + 50, 40 + 60); -- NULL
      SELECT NULLIF(50 + 50, 40 + 40); -- 100
      ```
    + ##### CASE
      ```mysql
      SET @age = 5;
      SELECT 
         CASE @age
             WHEN 0 THEN '영'
             WHEN 5 THEN '오'
             WHEN 10 THEN '십'
             ELSE '지정된 숫자가 아니다'
         END AS '결과';
      ```

- ### lambda
  - #### lambda 매개변수 ... : 표현식
    + ##### 함수를 간결하게 한 줄로 만들 때 사용
      ```python
      f = lambda x, y: print(x + y)
      f(5, 10)
      ```
- ### (local / global) variable
  - #### local variable
    + ##### 함수 안에서만 효용
      ```python
      v = 10          # 전역변수 (global variable)
      
      def scopeTest():
        v = 100       # 지역변수 (local variable)
      
      print(f'함수 안의 v = {v}')
      print(f'함수 밖의 v = {v}')  # 함수 밖의 v = 10
      scopeTest()                 # 함수 안의 v = 100
      print(f'함수 밖의 v = {v}')  # 함수 밖의 v = 10
      ```
  - #### global variable
    + ##### 함수 밖에서도 효용
      ```python
      v = 10      # global variable
      w = 20      # global variable
      
      def scopeTest():
        v = 100
        global w       # global variable로 선언
        w = 300
        print(f'함수 안의 v = {v}')
        print(f'함수 안의 w = {w}')
    
      print(f'함수 밖의 v = {v}')  # 함수 밖의 v = 10
      print(f'함수 밖의 w = {w}')  # 함수 밖의 w = 20
      scopeTest()                 # 함수 안의 v = 100, w = 300
      print(f'함수 밖의 v = {v}')  # 함수 밖의 v = 10
      print(f'함수 밖의 w = {w}')  # 함수 밖의 w = 300
      ```
- ### 외장 함수
  - #### import 사용
    + ##### datetime
      ```python
      import datetime
      
      now = datetime.datetime.now()
      print(f'오늘은 {now.year}년 {now.month}월 {now.day}일 입니다.')
      print(f'현재시간은 {now.hour}시 {now.minute}분입니다.')
      print(f'현재시간은 {now.hour - 12}시 {now.minute}분입니다.')
      
      today = datetime.datetime.today().weekday()
      if today == 0:
        print('월요일입니다')    # 0번이 월요일
      ```
- ### 외장 함수
  - #### 수학 관련
    + ##### abs, max, min
    ```python
    num = -10
    print(f'{num}의 절대값은 {abs(num)}')
    numList = [100, 45, 20, 40, 500]
    print(f'{numList}의 최대값은 {max(numList)}')
    print(f'{numList}의 최소값은 {min(numList)}')
    ```
    + ##### divmod(n1, n2)
    ```python
    print(f'55/2의 몫 = {divmod(55, 2)[0]}')
    print(f'55/2의 나머지 = {divmod(55, 2)[1]}')
    ```
    + ##### eval(문자열계산식)
    ```python
    result = input('수식을 입력하세요 ... ')
    print(result, ' = ', eval(result))      # 3+4 = 7
    ```
    
