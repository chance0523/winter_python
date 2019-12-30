# 수학관련 내장함수
# 절대값 리턴 : abs(숫자)
# 최대값 리턴 : max(리스트/튜플/집합...)
# 최소값 리턴 : min(리스트/튜플/집합...)

num = -10
print(f'{num}의 절대값은 {abs(num)}')
numList = [100, 45, 20, 40, 500]
print(f'{numList}의 최대값은 {max(numList)}')
print(f'{numList}의 최소값은 {min(numList)}')

numList2 = (100, 45, 20, 40, 500)
print(f'{numList2}의 최대값은 {max(numList2)}')
print(f'{numList2}의 최소값은 {min(numList2)}')

# 나누기 연산자 /, //
# 나머지 연산자 %
# divmod(n1,n2) => 몫과 나머지 값을 구한다. => 튜플
print(f'divmod(55,2) = {divmod(55,2)}, 데이터형 = {type(divmod(55,2))}')
print(f'55/2의 몫 = {divmod(55,2)[0]}')
print(f'55/2의 나머지 = {divmod(55,2)[1]}')
