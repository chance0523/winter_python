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
# 순서가 random하게 들어감
