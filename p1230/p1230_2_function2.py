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


printDict3(h='hippo', c='cat', m='mouse')
