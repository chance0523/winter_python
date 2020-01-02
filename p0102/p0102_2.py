# map() 함수
# map(정의된함수나 lambda함수,데이타(리스트,튜플))
# -> map오브젝트 생성
# list(map(정의된함수,데이타(리스트,튜플)))
# 데이타 요소를 정의된함수의 결과값으로 리턴한다.
# 결과값을 리스트 요소로 추가
print('\n퀴즈:리스트의 제곱을 구해서 새로운 리스트로 만들기  ')
numList2 = [1, 2, 3, 4]
print(numList2)
print('제곱값으로 구성된 리스트 출력(일반 함수)')


def power_fn1(list):
    result = []
    for i in list:
        result.append(i ** 2)
    return result


print(power_fn1(numList2))

print('제곱값으로 구성된 리스트 출력(map() 함수)')


def power_fn2(value):
    return value ** 2


# print(power_fn2(2))
print(map(power_fn2, numList2))
print(list(map(power_fn2, numList2)))

print('제곱값으로 구성된 리스트 출력(map(), lambda함수)')
f_multy = lambda x: x ** 2
# print(f_multy(2))
print(list(map(f_multy, numList2)))

print('\n퀴즈:두 리스트에서 인덱스가 같은 값을 서로 곱한 후 리스트로 만들기  ')

print('인덱스가 같은 두 수 곱하기 (일반 함수)')

print('인덱스가 같은 두 수 곱하기 (map 함수)')

print('인덱스가 같은 두 수 곱하기 (map(), lambda 함수)')

print('\n' * 2, '-' * 30)

# reduce()
# 외장함수로 import functools 모듈 임포트 명령 필요
# 리스트의 요소에 함수를 적용해 1개의 결과를 리턴한다.
print('\n퀴즈:리스트의 모든 합 구하기 ')
numList3 = list(range(1, 11))

print('\n일반함수 이용 ')


def sumList(list):
    sum = 0
    for i in list:
        sum += i
    return sum


print(sumList(numList3))

print('\nreduce() 이용 ')
import functools as f


def add(x, y):
    return x + y


print(f.reduce(add, numList3))

print('\nreduce(), lambda 이용')
f_add = lambda x, y: x + y
# print(f_add(1,2))
print(f.reduce(lambda x, y: x + y, numList3))
