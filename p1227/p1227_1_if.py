# 제어문의 종류
# 조건문 / 반복문

# if
# 단순 if문
a = 1
b = 10
if a > b:
    print('a는 b보다 크다.')
if a < b:
    print('a는 b보다 작다.')

# 홀짝 판단
myNum = 45
if myNum % 2 == 0:  # False
    print('짝수')
if myNum % 2 != 0:  # True
    print('홀수')
# if myNum % 2 is True:
#     print('True')
# if myNum % 2 is not True:
#     print('not True')

print('-' * 30)

'''
숫자를 입력해주세요 ...
3의 배수이다.
3의 배수가 아니다.
'''
# data = int(input('숫자를 입력해주세요 ... '))
# if data % 3 == 0:
#     print('3의 배수이다.')
# if data % 3 != 0:
#     print('3의 배수가 아니다.')

# 조건식에서 True가 되는 조건
# True, 0 빼고 나머지 숫자, 문자열
# 조건식에서 False가 되는 조건
# False, 0, '', None
# if True:
# if 123
# if -1:
if '문자열':
    print('무조건 실행')
# if False:
# if 0:
# if None:
if '':
    print('실행안됨')

# if ~ else
a2 = 1
b2 = 10
if a2 > b2:
    print('a2는 b2보다 크다.')
else:
    print('a2는 b2보다 작다.')
print('-' * 30)

# if ~ elif ~ else 다중 조건문
myData = 10
if myData == 0:
    print('0이다.')
elif myData > 0:
    print('양수이다.')
elif myData < 0:
    print('음수이다.')
else:
    print('숫자가 아니다.')

# 띠 테스트
result = 2009 % 12
animalList = ['원숭이', '닭', '개', '돼지', '쥐', '소', '범', '토끼', '용', '뱀', '말', '양']
print(f'{animalList[result]}띠 입니다!!!')
if result == 0:
    print("원숭이 띠 입니다!!!")
# ... #
