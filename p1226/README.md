# 12/26

- ### list

  - #### create / indexing / slicing
    ```python
    myList = [1, 2, 3, 4, 5]  # create`
    myList[0], myList[-1]     # indexing
    myList[:4], myList[1::2]  # slicing
    ```
  - #### function
    ```python
    myList.append('num')      # 맨 뒤에 삽입
    myList.insert(3, 'apple') # 특정 위치에 삽입
    myList.remove('num')      # 특정 요소 제거
    myList.pop()              # 맨 뒤 요소 제거
    myList.pop(0)             # 특정 위치 요소 제거
    myList.clear()            # 빈 리스트로 만들기
    del myList                # 리스트 삭제
    ```
  - #### function2
    ```python
    len(myList)                   # 리스트의 크기(길이)
    myList.sort()                 # 리스트 정렬
    myList.reverse()              # 리스트 요소를 역순으로
    myList.count(1)               # 특정 요소 갯수 세기
    myList.index('apple')         # 특정 요소의 위치
    myList.extend(['Seoul','NY']) # 여러개의 요소를 추가
    ```
  - #### casting

    ```python
    # 문자열 -> 리스트
    mkList = myStr.split()
    mkList = myStr.split(',')
    mkList = List(myStr)

    # 리스트 -> 문자열
    mkStr = str(myList)
    mkStr = '/'.join(myList)
    ```

- ### tuple

  - #### create / indexing / slicing
    ```python
    myTuple = (1, 2, 3, 4, 5)   # create
    myTuple = 'a','b','c'       # create
    myTuple[0], myTuple[-1]     # indexing
    myTuple[:4], myTuple[1::2]  # slicing
    ```
  - #### update / add

    ```python
    # update
    # Tuple can't update value

    # add
    myTuple += ('b',)
    myTuple += (100,)
    myTuple += (100, 200)
    ```

  - #### function
    ```python
    myTuple.count('num')      # 특정 요소의 갯수
    myTuple.index('apple')    # 특정 요소의 위치값
    myTuple.sort()            # ERROR !!!
    myTuple.reverse()         # ERROR !!!
    del myTuple               # 튜플 삭제
    ```
  - #### casting

    ```python
    # 문자열 -> 튜플
    # 리스트 -> 튜플
    mkTuple = tuple(myStr)
    mkTuple = tuple(myList)

    # 튜플 -> 문자열
    # 튜플 -> 리스트
    mkStr = str(myTuple)
    mkStr = '/'.join(myTuple)
    mkList = list(myTuple)
    ```

- ### dictionary

  - #### create / indexing

    ```python
     myDict = {100: '백', 200: '이백', 300: '삼백'}
     myDict =
     {'a': 'africa', 'c': 'cat', 'd': 'drama'} # create
     myDict[100], myDict['c']   # indexing : key로 조회
     # 중복키
     myDict = {'a': 'africa', 'c': 'cat', 'c': 'cafe'}
     # -> dict4 = {'a': 'africa', 'c': 'cafe'}
     # 키 값이 같으면 덮어 씌워짐.
    ```

  - #### function
    ```python
    myDict.pop('a')  # 특정 요소 삭제
    myDict.clear()   # 빈 딕셔너리로 만듬
    del myDict['c']  # 특정 요소 삭제
    del myDict       # 딕셔너리 삭제
    ```
  - #### dictionary function
    ```python
    myDict.values() # 값만 표시
    myDict.keys()   # 키값만 표시
    myDict.items()  # 전체 표시
    ```
  - #### casting

    ```python
    # 문자열 -> 튜플
    # 리스트 -> 튜플
    mkTuple = tuple(myStr)
    mkTuple = tuple(myList)

    # 튜플 -> 문자열
    # 튜플 -> 리스트
    mkStr = str(myTuple)
    mkStr = '/'.join(myTuple)
    mkList = list(myTuple)
    ```

- ### set
