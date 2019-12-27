# 12/27 - if, while, for
- ### if
  - #### if / if ~ else / if ~ elif ~ else
    + ##### if
      ```python
      a = 1
      b = 10
      if a > b:         # False
        print('a > b')
      if a < b:         # True
        print('a < b')
        ``` 
      ##### True면 실행, False면 실행 안 함.
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