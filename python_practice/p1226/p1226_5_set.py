# 집합
# {값1, 값2, 값3...}
# CRUD : Create Read Update Delete

# 집합의 생성
# 집합변수 = set(리스트/문자열/튜플)
# 순서가 없다. 랜덤하게 출력된다. 인덱싱이 불가능하다.(=슬라이싱 불가)
set1 = set('abcd')
set2 = set([100, 200, 400, 500])
set3 = set(('장미', '백합', '개나리'))
print(f'set1 = {set1}, type = {type(set1)}')
print(f'set2 = {set2}, type = {type(set2)}')
print(f'set3 = {set3}, type = {type(set3)}')
# set1 = {'a', 'd', 'c', 'b'}, type = <class 'set'>
# set2 = {200, 500, 100, 400}, type = <class 'set'>
# set3 = {'개나리', '백합', '장미'}, type = <class 'set'>
# 순서가 random하게 들어감

# 중복값을 허용할까요?
set4 = set([100, 200, 100, 50, 100])
print(f'set = {set4}')
# set = {200, 50, 100}
# 중복값을 허용하지 않고 하나만 표시함.
# indexing 불가능

# 집합의 요소 추가
# 집합변수.add(값)
# 집합변수.update(리스트)
set4.add(700)
print(f'after add 700 = {set4}')
set4.update([600, 100, 50, 1, 3])
print(f'after update = {set4}')

# 집합의 요소 삭제
set4.remove(1)
print(f'after remove 1 = {set4}')

del set4
# print(f'after del = {set4}') => ERROR!!!

# 집합의 연산
# +, *
userSet1 = set(['박', '이', '김', '최'])
userSet2 = set(['신', '김', '선우', '최'])
print('userSet1 = {}'.format(userSet1))
print('userSet2 = {}'.format(userSet2))
# 합집합
# set3 = set1 | set2
# set4 = set1.union(set2)
print('---합집합---')
userSet3 = userSet1 | userSet2
userSet4 = userSet1.union(userSet2)
print('userSet3 = {}'.format(userSet3))
print('userSet4 = {}'.format(userSet4))

# 교집합
# set3 = set1 & set2
# set4 = set1.intersection(set2)
print('---교집합---')
userSet3 = userSet1 & userSet2
userSet4 = userSet1.intersection(userSet2)
print('userSet3 = {}'.format(userSet3))
print('userSet4 = {}'.format(userSet4))

# 차집합
# set3 = set1 - set2
# set4 = set1.difference(set2)
print('---차집합---')
userSet3 = userSet1 - userSet2
userSet4 = userSet1.difference(userSet2)
print('userSet3 = {}'.format(userSet3))
print('userSet4 = {}'.format(userSet4))

# 캐스팅
# 리스트, 문자열, 튜플 -> 집합
# set(리스트, 문자열, 튜플)

# 집합 -> 리스트
# list(집합변수)
userList1 = list(userSet1)
print(f'userSet1 = {userSet1}, type = {type(userSet1)}')
print(f'userList1 = {userList1}, type = {type(userList1)}')

# 집합 -> 튜플
userTuple1 = tuple(userSet1)
print(f'userSet1 = {userSet1}, type = {type(userSet1)}')
print(f'userTuple1 = {userTuple1}, type = {type(userTuple1)}')

# 집합 -> 문자열
userStr1 = str(userSet1)
print(f'userSet1 = {userSet1}, type = {type(userSet1)}')
print(f'userStr1 = {userStr1}, type = {type(userStr1)}')

# 집합 -> 딕셔너리
userDict1 = dict(enumerate(userSet1))
print(f'userSet1 = {userSet1}, type = {type(userSet1)}')
print(f'userDict1 = {userDict1}, type = {type(userDict1)}')
