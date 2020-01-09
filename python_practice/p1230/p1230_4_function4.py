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
print(f'divmod(55,2) = {divmod(55, 2)}, 데이터형 = {type(divmod(55, 2))}')
print(f'55/2의 몫 = {divmod(55, 2)[0]}')
print(f'55/2의 나머지 = {divmod(55, 2)[1]}')

# enumerate(list/tuple/string, index number)
# enumerate 객체 생성
# for ... in 으로 하나씩 아이템 출력 가능
# 각각 튜플 아이템으로 생성 (인덱스, 값)
listA = ['a', 'b', 'c']
enumResult = enumerate(listA, 1)  # enumerate(list, start index num)
print(enumResult, type(enumResult))
for i in enumResult:
    print(i)

# enumResult => dictionary 구조로 변경
# dict(enumerate(list/string/tuple, index number)
listB = ['b', 'c', 'd']
enumResult2 = enumerate(listB, 1)
print(dict(enumResult2), type(dict(enumResult2)))

enumResult3 = enumerate(listA, 0)
for i, j in enumResult3:
    print(f'{i} => {j}')

# eval(문자열계산식)
# 입력받은 수식을 계산하여라
# result = input('수식을 입력하세요 ... ')
# print(result, ' = ', eval(result))

# 5개의 값을 입력문을 이용하여 리스트로 저장한 후
# 최대값과 최소값을 출력한다
# 빈 리스트를 생성
inList = []
for i in range(5):
    temp = int(input('숫자를 입력하세요 ... '))
    inList.append(temp)
print(max(inList), min(inList))

