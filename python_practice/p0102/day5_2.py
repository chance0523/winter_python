# map() 함수
# map(정의된함수나 lambda함수,데이타(리스트,튜플))
# -> map오브젝트 생성
# list(map(정의된함수나 lambda함수, 데이타(리스트,튜플)))
# 데이타 요소를 정의된함수의 결과값으로 리턴한다.
# 결과값을 리스트 요소로 추가
#
print('\n퀴즈:리스트의 제곱을 구해서 새로운 리스트로 만들기  ')
numlist2 = [1, 2, 3, 4]  # 결과 => [1, 4, 9, 16]

print('제곱값으로 구성된 리스트 출력(일반 함수)')


# 제곱을 구하는 함수 정의
def power_fn1(list):
    result = []
    for i in list:
        result.append(i ** 2)
    return result


print(power_fn1(numlist2))
# [1, 4, 9, 16]
print('제곱값으로 구성된 리스트 출력(map() 함수)')


# map() 사용할 제곱을 출력하는 함수 정의
def power_f2(value):
    return value ** 2


print(power_f2(3))  # 9
print(map(power_f2, numlist2))  # map 오브젝트로 출력
# 리스트화 해서 출력
print(list(map(power_f2, numlist2)))

print('제곱값으로 구성된 리스트 출력(map(), lambda함수)')
f_multy = lambda x: x ** 2
print(f_multy(2))  # 4
print(list(map(lambda x: x ** 2, numlist2)))
# [1, 4, 9, 16]

print('\n퀴즈:두 리스트에서 인덱스가 '
      '같은 값을 서로 곱한 후 리스트로 만들기  ')
list1 = [2, 3, 7]
list2 = [4, 5, 9]
# => [8, 15, 63]
print('인덱스가 같은 두 수 곱하기 (일반 함수)')


def multyply_n(list1, list2):
    resultList = []
    for i in range(0, len(list1)):
        resultList.append(list1[i] * list2[i])
    return resultList


print(list1, list2, '\n =>', multyply_n(list1, list2))
print('인덱스가 같은 두 수 곱하기 (map 함수)')


def multyply(x, y):
    return x * y


print(list1, list2, '\n =>',
      list(map(multyply, list1, list2)))

print('인덱스가 같은 두 수 곱하기 (map(), lambda 함수)')
f_multy2 = lambda x, y: x * y
print(f_multy2(2, 4))  # 8
print(list1, list2, '\n =>',
      list(map(lambda x, y: x * y, list1, list2)))

# print('\n'*2, '-'*30)

# reduce()
# 리스트의 요소에 함수를 적용해 1개의 결과를 리턴한다.
# reduce(람다나 정의한함수, 리스트나 튜플)
# 외장함수로 import functools 모듈 임포트 명령 필요
# 모듈내의 함수 사용1?
# import functools
# functools.reduce(옵션)
# 모듈내의 함수 사용2? = 별칭 지정
# import functools as f
# f.reduce(옵션)

print('\n퀴즈:리스트의 모든 합 구하기 ')
# 1~10으로 구성된 리스트 생성 : range()
numlist3 = list(range(1, 11))
print(numlist3)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('\n일반함수 이용 ')


def sumList(list):
    sum = 0
    for i in list:
        sum += i
    return sum


print(sumList(numlist3))  # 55
print('\nreduce() 이용 ')
import functools as f  # 모듈 임포트


def add(x, y):
    return x + y


print(f.reduce(add, numlist3))  # 55

print('\nreduce(), lambda 이용')
f_add = lambda x, y: x + y
print(f_add(1, 2))  # 3
print(f.reduce(lambda x, y: x + y, numlist3))  # 55

numlist10 = [True, 1, 'Yes', 2, 3, 5, 6, 'a']


def sumList2(list):
    sum = 0
    for i in list:
        if str(i).isdigit():
            sum += i
    return sum


print(sumList2(numlist10))

# f_addNum = lambda x, y: x + y if (type(x) == "<class 'int'>") and (y instance_of_integer) else 0
#
# print(f_addNum(10, 20))
# print(f_addNum(10, '20'))

# print(test(2,True))
# print(test(2,5))
# # print(f.reduce(lambda x:x.isdigit(), numlist10)
