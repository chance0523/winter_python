# 오류?
# 오류의 종류
# NameError: 함수이름, 변수, 리스트 이름등이 잘못된 경우
# IndexError :  튜플,리스트의 잘못된 인덱스 접근
# mylist = (1,)
# print(mylist[3])

# ZeroDivisionError : 0으로 나눈 경우
# print(23/0)

# FileNotFoundError : 잘못된 파일 경로
# SyntaxError 제외 => 예외처리 try: ~ Except 구문에서 제외

# 예외처리(Exception) 란?
# 오류가 발생을 하면 메세지를 출력하거나
# 오류를 무시하는 기능
# --------------------------
# 에러처리 문법 1

# try..except 명령1
# try:
#   명령어
# except 에러코드 as e:
#   에러처리명령

# try..except 명령2
# 모든 예외의 에러 메시지를 출력할 때는 Exception 키워드
# try:
#     명령
# except Exception as e:
#     print(e)

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

# try..except 명령3
# try:
#   명령어
# except:
#   에러처리명령`

try:
    print(v)
except:
    pass  # 에러 무시

# --------------------------
# 에러처리 문법 2
# try:
#   명령어
# except 에러코드 as e:
#   에러처리명령
# else:
#   에러가 발생하지 않은 경우 명령어
# try:
#     n1 = input('숫자1 입력 : ')
#     n2 = input('숫자2 입력 : ')
#     print(f'{n1}+{n2}={int(n1) + int(n2)}')
#
# except ValueError as e:
#     print('입력 데이터가 숫자가 아닙니다.\n\t\t %s' % e)

# 에러명을 모르는데 에러메세지는 출력하고 싶다
# try:
#   명령어
# except Exception as e:
#   e 출력 ,에러처리명령
# else:
#   에러가 발생하기 않은 경우 명령어


# --------------------------
# 에러처리 문법 3
# try:
#   명령어
# except 에러코드 as e:
#   에러처리명령
# else:
#   에러가 발생하기 않은 경우 명령어
# finally:
#   무조건 실행되는 명령어
try:
    f = open('data/없는파일.txt', 'r')
    print(f.readline())
except Exception as e:
    print(f'파일이 없습니다. \n\t\t {e}')
else:
    print(f.readline())
finally:
    print('-' * 20, '\n\t\t')

# try:
#   명령어
# except:
#   에러처리명령
# else:
#   에러가 발생하기 않은 경우 명령어
# finally:
#   무조건 실행되는 명령어


# --------------------------
# 에러처리 문법 4 : 오류 회피
# 에러 무시 : pass 키워드 사용
# try:
#   명령어
# except:
#   pass


# --------------------------
# 에러처리 문법 5
# 여러개의 오류 처리하기
# 먼저 발생한 오류 우선: 뒤에 오류는 실행되지 않음
'''
try:
    ...
except 발생오류1:
    에러메세지 출력1
except 발생오류2:
    에러메세지 출력2
'''


# --------------------------
# 에러만들기1 : raise 문 이용
# 일부러 에러 발생
# if 조건식:
#   raise Exception(오류 메세지)


# --------------------------
# 에러만들기2 : raise 문 이용
# 일부러 에러 발생


# --------------------------
# 에러만들기3 : Exception 내장 클래스 이용
# 특정 상황에서 예외 발생

# 1단계 : 사용자 에러 등록
# Exception 내장 클래스를 상속받아 임의의 에러명으로 클래스 생성
# class 에러명클래스(Exception):
#       명령문

class MyError(Exception):
    pass


# 함수 정의
# '바보' 문자열이 변수에 값으로 지정되면
# 정의된 myError() 발생

def say(nickName):
    if nickName == '바보':
        raise MyError()
    else:
        print('별명 ==>', nickName)


# 3단계 : 함수 호출
# say('천사')  # 별명 ==> 천사
# say('바보')

try:
    say('천사')
    say('바보')
except MyError:
    print('허용되지 않는 별명입니다.')


class MyError2(Exception):
    def __str__(self):
        return '허용되지 않는 별명입니다.'


try:
    say('천사')
    say('바보')
except MyError2 as e:
    print(e)
