# 퀴즈1 - 입력받은 값에 따라 양수와 음수를 출력하세요


# 퀴즈2   입력받은 숫자 값이 짝수이면  '숫자 : 짝수'
# 홀수이면 '숫자 : 홀수' 를 출력하세요
# 숫자%2 == 0 짝수
# 숫자%2 != 0 홀수


# 퀴즈 3 bmi 값에 따라 다음과 같은 메세지를 출력하세요
'''
bmi 값에 따라 출력한다.

k = 키(입력값) 단위 cm
w = 체중(입력값)

bmi = 체중(kg)/키(m)의제곱, 키의 단위는 미터(m)

bmi 값에 따라 다음과 출력한다.

고도 비만 : 35 보다 클 경우
중등도 비만  : 30 - 35 미만
경도 비만 : 25 - 30 미만
과체중 : 23 - 25 미만
정상 : 18.5 - 23 미만
저체중 : 18.5 미만
'''

'''
키를 입력해주세요... 단위 cm...180
체중을 입력해주세요... 단위 kg...95

bmi = 29.32
경도 비만
'''

# 퀴즈 4. 띠알아 맞추기
# 태어난 년도를 입력받아서 띠를 출력하세요
#
# 원숭이, 닭, 개, 돼지, 쥐, 소, 범, 토끼, 용, 뱀, 말, 양
# (0  ........  11)
#
# 띠 = 태어난년도%12

'''
태어난 년도를 입력하세요? ....   
당신이 태어난 년도는 (  ) 이고 (  )띠 입니다. 
'''


# 퀴즈 5
# 입력받은 나이에 따라 메세지를 출력하세요
#  age > 19 : 성인
#  17 <= age <= 19 : 고등학생
#  14 <= age < 17 : 중학생
#  8 <= age < 14 : 초등학생
#  age < 8  : 유치원생 또는 영유아

'''
당신의 나이를 입력해주세요 ... 12

당신은 초등학생 입니다.
'''


# 퀴즈 6
# 학점을 입력받아서 다음과 같은 메세지를 출력하세요
# score = float(input("학점 입력> "))
# if ~ elif ~ else 문 이용하여 메세지 출력
#
# 4.2 <= score <= 4.5 : 교수님의 사랑
# 3.5 <= score < 4.2 : 현 체제의 수호자
#  2.8 <= score < 3.5 : 일반인
# 2.3 <= score < 2.8  : 일탈을 꿈꾸는 소시민
# 2.3 미만 : 시대를 앞서가는 혁명의 씨앗

'''
학점 입력> 4.5

score = 4.5   : 교수님의 사랑 

'''

# 퀴즈 7 영어, 숫자 중 한 글자만 입력받은 후
# 입력값에 따라 다음과 같은 메세지를 출력하세요
#  조건문과 in 연산자 이용

# 숫자, 알파벳 리스트 만들기
# from string import ascii_lowercase
# from string import ascii_uppercase
#
# numList = list(range(0,10))
# lowercaseList = list(ascii_lowercase)
# uppercaseList = list(ascii_uppercase)

'''
영어, 숫자 중 한 글자만 입력하세요 ....A
입력한 데이타는 알파벳 입니다. 

영어, 숫자 중 한 글자만 입력하세요 ....1
입력한 데이타는 숫자 입니다. 

영어, 숫자 중 한 글자만 입력하세요 ....가 
입력한 데이타는 올바르지 않습니다. 영어, 숫자 중 한 글자만 입력하세요 
'''