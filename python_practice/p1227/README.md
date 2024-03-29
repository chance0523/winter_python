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
      if 'a' in 'banana':             # 'banana'에 'a'가 들어있나요?
        print('yes')
      if 'b' not in 'Python':         # 'Python'에 'b'가 들어있나요?
        print('no')
      if 1 in myList:                 # myList에 1이 들어있나요?
        print('yes')
      if 'python' not in myTuple:     # myTuple에 'python'이 들어있나요?
        print('no')
      if 'c' in mySet:                # mySet에 'c'가 들어있나요?
        print('yes')
        ```
- ### while
  - #### while / break / continue
    + ##### 조건이 True일 동안에 반복 수행
    + ##### while
      ```python
      # 1 ~ 100 까지의 합
      sum = 0
      a = 1
      while a <= 100:
          sum += a
          a += 1
      print(sum)  # 5050
      ```
    + ##### while문을 이용한 list, tuple, string, dictionary, set 출력 
      ```python
      # list
      i = 0
      list1 = ['사과', '바나나', '수박', '포도']
      while i < len(list1):
          print(i, '번째 요소는', list1[i])
      i += 1
        ```
    + ##### break, continue
      ```python
      # break는 while문을 빠져나옴
      count = 0
      while count < 2:
          print('Hello Python')
          count += 1
          break               # 만나면 while문 빠져나옴
      print('Hello Python2')
      
      # continue는 while문을 빠져나가지 않고 while문의 맨 처음으로 돌아감
      count = 0
      while count < 2:
          print('Hello Python')
          count += 1
          continue            # while문의 처음으로 돌아감
      print('Hello Python2')
        ``` 
- ### for
  - #### for / list 내부 for / for문으로 list 돌기
    + ##### for i in range(start, end, step):
      ```python
      sum = 0
      for i in range(1, 101):
          sum += i
      print('1~100까지의 합 :', sum)
       ```
    + ##### list 내부 for
      ```python
      numList = [i for i in range(1, 11)] # 1~10까지
      
      numList = [i * j for i in range(2, 11) for j in range(1, 10)] # 구구단
      ``` 
    + ##### for문으로 list돌기 (문자열, 튜플, 딕셔너리(키 or 값)도 가능)
      ```python
      # list
      myList = [2, 3, 5, 7, 11]
      for i in myList:
          print(i, end=' ')
      
      # string
      myText = '가나다라마바사'
      for i in myText:
          print(i, end=' ')
      
      # 다중 리스트
      listMulti2 = [[1, 2, 3],
              ['a', 'b', 'c'],
              ['홍길동', '춘향이', '이몽룡']]
      for (i, j, k) in listMulti2:
          print(i, j, k)
      ```
