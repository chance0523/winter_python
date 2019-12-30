# 가변인자 : 인자의갯수가 정해지지 않는 경우
# def 함수명(*args):

def studentName(*args):
    print(args)


studentName('홍길동')
studentName('홍길동', '이영희')
studentName('홍길동', '이영희', '이순신')

# 퀴즈1. 위의 예제를 다음 형태로 변경하여라
'''
1번 학생 : ?
2번 학생 : ?
...
'''


def studentName2(*args):
    print(args)
    for i in range(len(args)):
        print(i + 1, '번 학생 :', args[i])


studentName2('홍길동')
studentName2('홍길동', '이영희')
studentName2('홍길동', '이영희', '이순신')


# quiz2
# n개의 숫자의 합을 구하는 가변함수
def sumNumber(*args):
    sum = 0
    for i in range(len(args)):
        sum += args[i]
    print('총합은', sum)


sumNumber(1, 2)
sumNumber(4, 5, 6)


# 인자와 가변인자가 함께
def printSymbolNumber(symbol, *args):
    return print(f'{symbol} // {args}')


printSymbolNumber('##', 10)
printSymbolNumber('$$$', 10, 20, 30)
'''
## // (10,)
$$$ // (10, 20, 30)
'''


# **kwargs
def printDict(**kwargs):
    return print(kwargs)


printDict(key1='zl1')
printDict(key1='zl1', key2='zl2')


def printDict2(**kwargs):
    print(f'kwargs[key1] = {kwargs["key1"]}')


printDict2(key1='hippo', key2='cat')


def printDict3(**kwargs):
    print(kwargs['h'])
    print(kwargs['c'])
    print(kwargs['c'])
    print(kwargs['m'])
    for key in kwargs:
        print(f'{key} : {kwargs[key]}')


printDict3(h='hippo', c='cat', m='mouse')


# item in group / item not in group
# print('a' in 'banana')
# print('a' not in 'banana')


# 초기값을 정해주지 않지만 default 값은 'USA'로 정해줌
def makePerson2(**kwargs):
    # kwargs['nationlity'] = 'USA' => 이렇게 쓰면 초기값을 정해줌
    if 'nationality' not in kwargs:
        kwargs['nationality'] = 'USA'
    print('-' * 20)
    for key in kwargs:
        print(f'{key}={kwargs[key]}')


makePerson2(age=13, name='Sopia', nationality='Spain')


# 람다함수
# lambda
# 함수변수 = lambda 인자 : 명령

# 문자열을 특정 단어와 결합해서 출력한다.
# def 사용
def printWord(m):
    return 'Message => ' + m


print(printWord('오늘도 좋은 하루'))

# lambda 사용
f1 = lambda message: 'Message => ' + message
print(f1('좋은 하루되세요'))

# 두 수의 합을 출력한다.
f2 = lambda x, y: print(f'{x} + {y} = {x + y}')
f2(5, 10)
f = lambda x, y: print(x + y)
f2(5, 10)

# 함수의 변수 영역
# 스코프(Scope)
# 전역변수(문서 전체의 공통변수)
# 지역변수

v = 10  # 전역변수
def scopeTest():
    v = 100  # 지역변수
    print(f'함수 안의 v = {v}')
print(f'함수 밖의 v = {v}')  # 함수 밖의 v = 10
scopeTest()  # 함수 안의 v = 100
print(f'함수 밖의 v = {v}')  # 함수 밖의 v = 10

print('-' * 30)

# 함수 내에게서 지역변수를 전역변수로 정의
v = 10
w = 20
def scopeTest():
    v = 100
    global w
    w = 300
    print(f'함수 안의 v = {v}')
    print(f'함수 안의 w = {w}')


print(f'함수 밖의 v = {v}')
print(f'함수 밖의 w = {w}')
scopeTest()
print(f'함수 밖의 v = {v}')
print(f'함수 밖의 w = {w}')
