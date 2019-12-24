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