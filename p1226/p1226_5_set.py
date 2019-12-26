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
