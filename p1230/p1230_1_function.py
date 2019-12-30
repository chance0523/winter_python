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

