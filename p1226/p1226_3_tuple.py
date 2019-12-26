# tuple
# CRUD : Create Read Update(Add)

# tuple 생성 (초기값 지정)
# 튜플 변수 = (값1, 값2...)
t1 = (100, 200, 300)
t2 = ('a')
print(f't1 = {t1}, type = {type(t1)}')
print(f't2 = {t2}, type = {type(t2)}')

# 튜플 생성2 (초기값 지정)
# 튜플 변수 = 값1, 값2
t3 = '가', '나', '다'
print(f't3 = {t3}, type = {type(t3)}')

# 튜플 생성3 (빈 튜플)
t4 = ()
print(f't4 = {t4}, type = {type(t4)}')

# tuple indexing
# tuple[indexing number]
# tuple slicing
# tuple[start:end:step]
t5 = (100, 200, 300, 400)
print(f't5[0] = {t5[0]}, type = {type(t5[0])}')
print(f't5[:2] = {t5[-1]}, type = {type(t5[-1])}')
print(f't5[:2] = {t5[:2]}, type = {type(t5[:2])}')
print(f't5[1:3] = {t5[1:3]}, type = {type(t5[1:3])}')

# tuple update
'''
print(f't2 = {t2}')
t2[0] = 'python' -> TYPE ERROR !!!
print(f't2 = {t2}')
'''

# 튜플은 값을 새로 추가 할 수 있는가?
# 튜플변수 += 값
# 튜플변수 += (값1, 값2...)
# 한 개 추가시에는 쉼표(,) 주의
print(f't2 = {t2}')
t2 += 'b'
print(f't2 = {t2}')
t2 += ('c')
print(f't2 = {t2}')
t6 = (100, 200, 300)
print(f't6 = {t6}')
t6 += ('add',)
print(f't6 = {t6}')
t6 += (400,)
print(f't6 = {t6}')
t7 = (100, 200)
print(f't7 = {t7}')
print(f't6 + t7 = {t6 + t7}')
t8 = ('8',)
print(f't8 = {t8}')
print(f't8 = {t6 + t8}')

# 튜플의 값은 삭제가 가능한가?
del t8
# print(f't8 = {t8}') -> 사라짐. name error

# 튜플의 연산자
t5 = ('python', 'java')
t6 = ('mysql',)
print(f't5 = {t5}')
print(f't6 = {t6}')
print(f't5 + t6 = {t5 + t6}')
print(f't5*3 = {t5 * 3}')

# 각각 튜플 변수 정의하기
# 튜플전체변수 = (변수1, 변수2...)=(값1, 값2...)
colorTuple = (c1, c2) = ('red', 'blue')
print(f'colorTuple = {colorTuple}')
print(f'colorTuple[0] = {colorTuple[0]}')
print(f'c1 = {c1}')
print(f'c2 = {c2}')

# tuple function
# 튜플변수.count(값)
# 튜플변수.index(값)
# 튜플변수.sort()    -> 가능한가?
# 튜플변수.reverse() -> 가능한가?
numberTuple = (100, 1, 2, 50, 777, 1, 1)
print(f'numberTuple = {numberTuple}')
print(f'nubmerTuple에서 1의 갯수 = {numberTuple.count(1)}')
print(f'numberTuple에서 50의 위치값 = {numberTuple.index(50)}')
# print(f'numberTuple sort = {numberTuple.sort()}') => ERROR!!!
# print(f'numberTuple reverse = {numberTuple.reverse()}') => ERROR!!!

# casting
# 문자열 => 튜플 : tuple(문자열변수나 값)
# 리스트 => 튜플 : tuple(리스트변수나 값)
txt1 = "우리나라 좋은나라"
list1 = [100, 200, 300]
print(f'txt1 = {txt1}, type = {type(txt1)}')
print(f'list1 = {list1}, type = {type(list1)}')
txt1Tuple = tuple(txt1)
print(f'txt1Tuple = {txt1Tuple}, type = {type(txt1Tuple)}')
list1Tuple = tuple(list1)
print(f'list1Tuple = {list1Tuple}, type = {type(list1Tuple)}')

# 튜플 => 문자열 : str(tuple), 구분자.join
# join 사용 시에는 튜플의 자료형이 문자열이어야한다.
# 튜플 => 리스트 : list(tuple)
txt2 = str(txt1Tuple)
print(f'txt2 = {txt2}, type = {type(txt2)}')
txt3 = '/'.join(txt1Tuple)
print(f'txt3 = {txt3}, type = {type(txt3)}')
list2 = list(list1Tuple)
print(f'list2 = {list2}, type = {type(list2)}')

# 튜플 리스트
foodT1 = ('고구마', '감자')
foodT2 = ('짬뽕', '짜장면', '라면')
foodList = [foodT1, foodT2]
print(f'foodT1 = {foodList}, type = {type(foodList)}')
print(f'foodT1 = {foodList[0]}, type = {type(foodList[0])}')
print(f'foodT1 = {foodList[1]}, type = {type(foodList[1])}')

# quiz #
'''
아래와 같이 튜플을 정의한 후 출력한다.
튜플 리스트 : ('강아지', '토끼', '돼지', '곰')
튜플 요소 추가 후 : ('강아지', '토끼', '돼지', '곰', '호랑이')
튜플의 0~3번째 요소 표시 : ('강아지', '토끼', '돼지', '곰)
'강아지' 요소의 위치값은?
튜플을 문자열로 변환하여 출력 : 강아지, 토끼, 돼지, ...
튜플을 리스트로 변환하여 출력 : 
'''

print('---quiz---')
animal=('강아지', '토끼', '돼지', '곰')
print(f'튜플 리스트 : {animal}')
animal+=('호랑이',)
print(f'튜플 요소 추가 후 : {animal}')
print(f'튜플의 0~3번째 요소 표시 : {animal[:4]}')
print(f'"강아지" 요소의 위치값은? : {animal.index("강아지")}')
strAnimal=', '.join(animal)
listAnimal=list(animal)
print(f'튜플을 문자열로 변환하여 출력 : {strAnimal}')
print(f'튜플을 리스트로 변환하여 출력 : {listAnimal}')

