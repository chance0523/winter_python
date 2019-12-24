# 한 줄 주석
'''
여러줄
주석
'''
print(1)
print(100)
print('Hello World!')
print(100,'+',200,'=',100+200)

# end
print(True)
print(False)
print(True,False)
print(True,end=' ')
print(False)

# 문자열 연산자
print('Hello'+"World")
print('a'*3)

# 변수
txt1='Hello'
txt2=' world'
print(txt1+txt2)
print(txt1*3+txt2*2)
print('-'*20)

# escape
# \n, \t, \\, \', \"
print("'hello'")
print("\'hello\'")
print("\n\n\t'점심 시간 안내'")
print('-'*20,'\n','**\t12시-1시')
print('-'*20)

# 변수 할당
# 서로 다른 변수에 동일한 값
num1=100
num2=100
num3=num4=100
print(num1,num2,num3,num4)
num5,num6=200,300
print(num5,num6)


# quiz : user1, user2의 변수값을 서로 변경하여라
user1='영희'
user2='철수'
print('user1 = ',user1)
print('user2 = ',user2)
user1,user2=user2,user1
print('user1 = ',user1)
print('user2 = ',user2)

# 변수명 정의방식
# 카멜 표기법 : 대문자, 소문자 섞어서
# userAge
# 스네이크 기법 : _, - 단어 연결
# user_age
'''
클래스명은 첫글자를 대문자로
함수명은 소문자로 표시
변수명은 소문자로 시작
예약어는 변수명으로 사용할 수 없다
파이썬 예약어(keyword) 출력하기
'''
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))