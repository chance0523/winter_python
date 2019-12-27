# 12/27 - if, while, for
- ### if
  - #### if / if ~ else / if ~ elif ~ else
    + ##### 조건이 True면 실행, False면 실행 안 함.
    + ##### if
      ```python
      a = 1
      b = 10
      if a > b:         # False
        print('a > b')
      if a < b:         # True
        print('a < b')
        ``` 
    + ##### if ~ else
      ```python
      if a > b:
        print('a > b')
      else:
        print('a <= b')
        ```
    + ##### if ~ elif ~ else
      ```python
      if a > b:
        print('a > b')
      elif a < b:
        print('a < b')
      else:
        print('a == b')
      ```
    + ##### in, not in을 활용한 if문
      ```python
      if 'a' in 'banana':
        print('yes')
      if 'b' not in 'Python':
        print('no')
      if 1 in myList:
        print('yes')
      if 'python' not in myTuple:
        print('no')
      if 'c' in mySet:
        print('yes')
        ```
- ### while
  - #### 조건이 True일 동안에 반복 수행
    + ##### 기본 while문
    ```python
    sum = 0
    a = 1
    while a <= 100:
        sum += a
        a += 1
    print(sum)  # 5050
    ```
  
