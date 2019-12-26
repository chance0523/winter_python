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

dict5 = {'a': 'africa', 'af': 'africa', 'c': 'coffee','d':'dry'}
print(f'dict5 = {dict5}')
'''
dict5 = {'a': 'africa', 'af': 'africa', 'c': 'coffee', 'd': 'dry'}
값은 같아도 된다.
'''

# 딕셔너리 값 교체
# 딕셔너리[키값] = 값
dict5['d']='drama'
print(f'dict5 = {dict5}')
'''
dict5 = {'a': 'africa', 'af': 'africa', 'c': 'coffee', 'd': 'drama'}
'''

# 딕셔너리 요소 삭제
# 딕셔너리 변수
