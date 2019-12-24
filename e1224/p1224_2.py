''''''
'''
multi line print
-개행문자 \n 이용
- 문자열 내용 이용
'''

print('안\n녕\n**')
print('''
안
녕
**''')

# 정의된 변수 삭제
# del 변수명
a = 200
print('a는?', a)
a = 100
print('a는?', a)
del a
# print(a)
# NameError : name 'a' is not defined


'''
입력문
변수명 = input()
입력받은 변수는 데이터형이 문자열이다.
'''
# message = input('메세지를 입력하세요? ... ')
# print(message)

'''
데이터형 확인하기
type(변수/값)
자료형의 종류
- 기본자료형
: 숫자형(정수, 실수, 16진수, 8진수)
: 문자열
: Boolean - True / False
- 집합자료형
: list, tuple, dictionary, class, set
'''

print(type(True))
print(type(111))
print(type("Python"))
print(type(34.5))

# message = input("메세지를 입력하세요 ... ")
# print('message = ',message)
# print(type(message))

# 16진수 : 0x00
# 8진수 : 0o00
print('16진수 : ', 0xF1)
print('8진수 : ', 0o53)

# 대입 연산자
print(100 + 20 * 40)
print((100 + 20) * 40)
myNum3 = 100
print('myNum3 = ', myNum3)
myNum3 += 10
print('myNum3 = ', myNum3)
myNum3 /= 10
print('myNum3 = ', myNum3)

# 관계 연산자
# 결과 값 : True, False
print(100 > 10)
print(100 >= 10)
print(100 == 10)
print(100 != 10)

# 논리 연산자
# and, or, not
print('논리연산자')
x = 10
y = 100
# (x < y) == True
# (x == y) == False
print((x < y) and (x == y))
print((x < y) or (x == y))
print(not (x < y))

# is, is not 연산자
# 값이 같은지 비교한다.
# 결과값이 T/F
stName1 = 'high'
stName2 = 'low'
stName3 = 'High'
print('is 연산자')
print(stName1 is stName2)
print(stName1 is not stName2)
print(stName1 is stName3)
# 당연하게 대소문자 구분

