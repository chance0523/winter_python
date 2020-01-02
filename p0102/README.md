# 01 / 02 - function / lambda / (local, global) variable
- ### 사용자 정의 함수
  - #### 단순 인자 => def function_name ( ... ):
    + ##### 인자 x, return 값 x
      ```python
      def helloWorld():
        print('Hello world' * 3)
      helloWorld()
        ``` 
    + ##### 인자 o, return 값 x
      ```python
      def messagePrint(message):
        print(message * 3)
      messagePrint('Hello world * 3')
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