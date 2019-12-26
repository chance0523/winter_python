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
dict3[1] = '이영애'
print(f'dict3 = {dict3}')

# 딕셔너리 요소 조회 (indexing)
# 딕셔너리 변수[키값]
print(f'dict3[1] = {dict3[1]}')
# print(f'dict3[0] = {dict3[0]}') => ERROR!!!
print(f'dict3["st1"] = {dict3["st1"]}')
