# function
# 내장함수 : import 명령없이 사용할 수 있는 함수 (len, type ... )
# 사용자정의함수 : def 명령으로 정의하는 함수

# 함수의 종류
# 결과값은 return 문으로 전달
# 인자 x, 결과값 x => 단순함수
# 인자 o, 결과값 x
# 인자 o, 결과값 o

# 인자의 종류
# 단순인자
# 초기값 지정 인자
# 가변인자
# 딕셔너리 가변인자

# 인자 x, 결과값 x
def helloWorld():
    print('Hello world\t' * 3)


helloWorld()


# 인자 o, 결과값 x
def messagePrint(message):
    print(message * 3)


messagePrint('hello world \t')
messagePrint('hello python\t')


def addNum(a, b):
    print(a, '+', b, '=', a + b)


addNum(1, 2)  # 1+2
addNum(500, 40000)


# 인자 x, 결과값 o
def classPrint():
    return 'MySQL, sqLite'


# 함수호출
# classPrint() 만으로는 아무것도 안 뜸
print(classPrint())


def classPrint2():
    message1 = 'Pytorch'
    message2 = 'Tensorflow'
    return message1, message2


print(classPrint2())  # tuple print


def classPrint3():
    message1 = 'JAVA'
    message2 = 'VUE'
    return message2  # 이것만 return . 마치 break
    message2 += message1
    return messag2


print(classPrint3())


# quiz
# 2개의 인자를 받아서 사칙연산
def cal(a, b):
    print(a, '+', b, '=', a + b)
    print(a, '-', b, '=', a - b)
    print(a, '*', b, '=', a * b)
    print(a, '/', b, '=', a / b)


cal(30, 3)
print('-' * 30)


# 인자 o, 결과값 o
def messagePrint2(m):
    return 'Happy New Year ' + m + '님'


print(messagePrint2('홍길동'))


# 숫자를 받아서 1 ~ 숫자까지의 합 구하기
def sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


print(sum(100))


def sum2(x, y):
    sum = 0
    for i in range(x, y + 1):
        sum += i
    return sum


print(sum2(30, 100))

# quiz
# n개의 입력을 받아서 리스트에 저장하는 함수 정의
'''
def savelist(n):
    myList = []
    for i in range(n):
        myList.append(input('입력 : '))
    return myList


print(savelist(3))
'''


# 인자 o, return 값 다중
def mulitReturn(n, m):
    return n + m, n - m


print(mulitReturn(2, 3))  # tuple


# 인자의 초기값 설정
def sum3(n=0, m=0):
    return n + m


print(f'sum3() = {sum3()}')
print(f'sum3(10) = {sum3(10)}')
print(f'sum3(2, 3) = {sum3(2, 3)}')
