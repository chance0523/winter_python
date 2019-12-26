# dictionary
# CRUD : Create Read Update Delete

# dictionary 생성
# 초기값 지정
# 딕션너리 변수 = {키1:값1, 키2:값2, ... }
# 키값은 문자형, 숫자형 둘 다 가능
dict1 = {100: '백', 200: '이백', 300: '삼백'}
dict2 = {'a': 'africa', 'c': 'cat', 'd': 'drama'}
print(f'dict1 = {dict1}, type = {type(dict1)}')
print(f'dict2 = {dict2}, type = {type(dict2)}')

# 빈 딕셔너리 생성
dict3 = {}
print(f'dict3 = {dict3}, type = {type(dict3)}')

# 딕셔너리 추가
# 딕셔너리변수[키값] = 값
dict3['st1'] = '홍길동'
print(f'dict3 = {dict3}')
dict3[22] = '이영애'
print(f'dict3 = {dict3}')

# 딕셔너리 요소 조회 (indexing)
# 딕셔너리 변수[키값]
print(f'dict3[22] = {dict3[22]}')
# print(f'dict3[0] = {dict3[0]}') => ERROR!!!
# 딕셔너리는 키값으로만 호출가능 (숫자인덱싱 x)
print(f'dict3["st1"] = {dict3["st1"]}')
# print(f'dict3[0:2] = {dict3[0:2]}') => ERROR!!!

# 딕셔너리 중복키는 가능할까요?
dict4 = {'a': 'africa', 'c': 'cat', 'c': 'coffee'}
print(f'dict4 = {dict4}')
'''
dict4 = {'a': 'africa', 'c': 'coffee'}
키 값이 같으면 덮어 씌워짐.
'''

dict5 = {'a': 'africa', 'af': 'africa', 'c': 'coffee', 'd': 'dry'}
print(f'dict5 = {dict5}')
'''
dict5 = {'a': 'africa', 'af': 'africa', 'c': 'coffee', 'd': 'dry'}
값은 같아도 된다.
'''

# 딕셔너리 값 교체
# 딕셔너리[키값] = 값
dict5['d'] = 'drama'
print(f'dict5 = {dict5}')
'''
dict5 = {'a': 'africa', 'af': 'africa', 'c': 'coffee', 'd': 'drama'}
'''

# 딕셔너리 요소 삭제
# 딕셔너리변수.clear()
# 딕셔너리변수.pop(키값)
# del 딕셔너리변수
# del 딕셔너리변수[키값]
print('-' * 30)
print(f'dict5 = {dict5}')
dict5.pop('a')
print(f'dict5 = {dict5}')
del dict5['c']
print(f'dict5 = {dict5}')
dict5.clear()
print(f'dict5 = {dict5}')
del dict5
# print(f'dict5 = {dict5}') => ERROR!!! 이미 지워짐

# 딕셔너리 함수
# 딕셔너리 변수.values() : 값만 표시
# 딕셔너리변수.keys() : 키값만 표시
# 딕셔너리변수.items() : 전체 표시
dict5 = {'a': 'africa', 's': 'say', 'c': 'coffee', 'd': 'drama', 'y': 'yes'}
print(f'dict5 = {dict5}')
print(f'dict5.values() = {dict5.values()}')
print(f'dict5.keys() = {dict5.keys()}')
print(f'dict5.items() = {dict5.items()}')

# 딕셔너리에 키값만 리스트로 만들어서 마지막 키값 조회
keysList = dict5.keys()
print(f'keysList = {keysList}')
# print(f'keysList[-1] = {keysList[-1]}') => TYPE ERROR !!!
keysList = list(keysList)  # list로 바꿔줌
print(f'keysList = {keysList}')
print(f'keysList[-1] = {keysList[-1]}')

print('--- 캐스팅 ---')
# 딕셔너리 => 리스트
dict6 = {'a': 'africa', 's': 'say', 'c': 'coffee', 'd': 'drama', 'y': 'yes'}
# 값만 모아서 리스트로
dict6ValuesList = list(dict6.values())
print(f'dict6ValuesList = {dict6ValuesList}, type = {type(dict6ValuesList)}')

# 키만 모아서 리스트로
dict6ValuesList = list(dict6.keys())
print(f'dict6ValuesList = {dict6ValuesList}')
dict6ValuesList = list(dict6)
print(f'dict6ValuesList = {dict6ValuesList}')

# 리스트 => 딕셔너리 : (인덱싱 숫자가 키가 됨)
# dict()
# enumerate() : 리스트, 문자열, 튜플 같은 자료형을 enumerate 객체로 반환
# enumerate 객체의 요소는 딕셔너리 스타일, 키값은 숫자로 표시
myList = ['Red', 'Blue', 'Green']
print(f'myList = {myList}')
# myDict = dict(myList) -> ERROR!!!
temp = enumerate(myList)
print(f'temp = {temp}')
# temp = <enumerate object at 0x00000144AF7D4E00>
# for i in temp:
#     print(i)
'''
(0, 'Red')
(1, 'Blue')
(2, 'Green')
'''
# 한 번 풀리면 다시 안 묶임 !!!
for key, value in temp:
    print(key, value)
'''
0 Red
1 Blue
2 Green
'''
# print(f'myDict = {myDict}')

# 리스트 => enumerate() => dict()
myList2 = ['Red', 'Blue', 'Green']
myDict2 = dict(enumerate(myList2))
print(f'myDict2 = {myDict2}')
print(f'myDict2 type = {type(myDict2)}')

# 딕셔너리 => 문자열
# str(딕셔너리변수) => { : , :  , ...}
# 구분자.join(딕셔너리변수) => 키값으로 생성
dict7 = {'a': 'africa', 's': 'say', 'c': 'coffee', 'd': 'drama', 'y': 'yes'}
print(f'dict7 = {dict7}, type = {type(dict7)}')
print(f'문자열로 변경 = {str(dict7)}, type = {type(str(dict7))}')
print(f'문자열로 변경 = {",".join(dict7)}, type = {type(",".join(dict7))}')

# 딕셔너리 => 튜플
# tuple() => 키값으로 이루어진 튜플
print(f'튜플로 변경 = {tuple(dict7)}, type = {type(tuple(dict7))}')
# 딕셔너리 값으로만 이루어진 튜플 생성
print(f'dict7.values()? {dict7.values()}')
print(f'tuple(dict7.values())? {tuple(dict7.values())}')

# 딕셔너리 리스트
# 리스트 안에 딕셔너리가 있는 구조
dictList = [{'a': 'apple', 'v': 'victory'},
            {100: '백', 200: '이백'},
            {'user1': '김철수', 'user2': '고소영'}
            ]
print(f'dictList = {dictList}')
print(f'dictList[0] = {dictList[0]}')
print(f'dictList[0]["a"] = {dictList[0]["a"]}')
print(f'dictList[2][\'user1\'] = {dictList[2]["user1"]}')
