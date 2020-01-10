# 1/10 - variable
- ### variable
  - #### create variable
    + ##### SET @variable_name;
      ```mysql
      SET @a = 1;
      SET @b = 'MySQL';
      ```
    + ##### (cast / convert) variable type
      ```mysql
      -- 실수 => 양의 정수
      SELECT
          CAST(AVG(amount) AS SIGNED INTEGER) AS '평균 구매 갯수'
      FROM buyTbl;
      ```
    + ##### 인자 x, return 값 x
      ```python
      def classPrint():
        return 'MySQL, sqLite'
      print(classPrint())
      ```
    + ##### 인자 o, return 값 o
      ```python
      def sum(n):
        sum = 0
        for i in range(1, n + 1):
        sum += i
        return sum
      print(sum(100))
      ```
    + ##### 다중 return
      ```python
      def multiReturn(n, m):
        return n + m, n - m
      print(multiReturn(2, 3)) # tuple로 return
      ```
  - #### 가변 인자 => def function_name (*args):
    + ##### *args
      ```python
      def studentName(*args):
        print(args)
      studentName('Jake')
      studentName('Jake','Amy')
      studentName('Jake','Amy','Tilda')
      ```
    + ##### *kwargs
      ```python
      def printDict(**kwargs):
        print(kwargs)            # dictionary 출력
        print(kwargs['key1'])    # 'key1'의 값 출력
      printDict(key1 = 'hippo', key2 = 'cat')
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
    
