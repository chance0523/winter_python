# 12/30 - function
- ### 사용자 정의 함수
  - #### def function_name ( ... ):
    + ##### 인자 x, 결과값 x
      ```python
      def helloWorld():
        print('Hello world' * 3)
      helloWorld()
        ``` 
    + ##### 인자 o, 결과값 x
      ```python
      def messagePrint(message):
        print(message * 3)
      messagePrint('Hello world * 3')
      ```
    + ##### 인자 x, 결과값 x
      ```python
      def classPrint():
        return 'MySQL, sqLite'
      print(classPrint())
      ```
    + ##### 인자 o, 결과값 o
      ```python
      def sum(n):
        sum = 0
        for i in range(1, n + 1):
        sum += i
        return sum
      print(sum(100))
      ```