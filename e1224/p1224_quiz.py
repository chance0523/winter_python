# 퀴즈 1:
# 아래와 같이 3줄로 글자를 출력하는 4가지 방법은?
'''
파이썬
파이썬
파이썬
'''

print('---quiz1---')
print('방법1')
print('파이썬\n파이썬\n파이썬')
print('\n방법2')
print('파이썬')
print('파이썬')
print('파이썬')
print('\n방법3')
print('파이썬\n' * 3)
print('\n방법4')
a = '파이썬'
print(a)
print(a)
print(a)
print()

# 퀴즈 2
# 홍길동 씨의 과목별 점수는 다음과 같다.
# 홍길동 씨의 평균 점수를 소숫점 둘째자리까지 출력하여라
'''
국어 : 86
영어 : 77
수학 : 55
평균 : 
'''

print('---quiz2---')
korean = 86
english = 77
math = 55
average = (korean + english + math) / 3
print("평균 = %.2f점" % average)
print()

# 퀴즈 3
# 변수 a,b를 입력문을 이용하여 데이터를 저장한다.
# == 을 이용하여 a,b 가 같은지 True, False 로 출력하여라
'''
a ? 10
b ? 10
True
'''

print('---quiz3---')
a = int(input('a ? '))
b = int(input('b ? '))
print(a == b)
print()

# 퀴즈 4
# 2개의 숫자를 입력받아
# 사칙연산의 결과물을 출력하여라
# 출력시 % 포맷 형식 이용

'''
첫번째 숫자를 입력하세요? 34
두번째 숫자를 입력하세요? 56

결과 :
34 + 56 = 
34 - 56 =
34 * 56 =
34 / 56 =

'''

print('---quiz4---')
n1 = int(input('첫번째 숫자를 입력하세요? '))
n2 = int(input('두번째 숫자를 입력하세요? '))

print('%d + %d = %d' % (n1, n2, n1 + n2))
print('%d - %d = %d' % (n1, n2, n1 - n2))
print('%d * %d = %d' % (n1, n2, n1 * n2))
print('%d / %d = %d' % (n1, n2, n1 / n2))
print()

# 퀴즈 5
# 홍길동씨의 주민등록번호는 881120-1068234
# 연월일과 숫자 부분을 나누어서 출력하여라.
'''
연월일 : 881120
숫자 : 1068234
'''

print('---quiz5---')
hongsJoo = '881120-1068234'
print('연월일 :', hongsJoo[:6])
print('숫자 :', hongsJoo[-7:])
print()

# 퀴즈 6
# 2개의 변수를 정의하고 아래와 같이 출력한다.
# format 이용

'''
movie1 = '알라딘'
movie2 = '스파이더맨'

--------------
스파이더맨      :        알라딘
+++   알라딘    +++

'''

print('---quiz6---')
movie1 = '알라딘'
movie2 = '스파이더맨'
print('{:<10} : {:>10}'.format(movie2, movie1))
print('+++{:^10}+++'.format(movie1))
print()

# 퀴즈 7
# 다음과 같이 교체한다.
# replace() 이용

'''
좋아하는 꽃 - 장미 

좋아하는 꽃 - 백합 

좋아하는 flower - 백합 
'''

print('---quiz7---')
src = '좋아하는 꽃 - 장미'
print(src)
dst1 = src.replace('장미', '백합')
print(dst1)
dst2 = dst1.replace('꽃', 'flower')
print(dst2)
print()

# 퀴즈 8
# 다음과 같이 문자열 변수를 정의하고 결과값이 출력되도록 한다.
'''
Let thy speech be short, comprehending much in few words.

첫번째 t의 위치 : 3
첫번째 m의 위치 : 28
s 의 갯수 : 3

= 으로 연결 : 
 L=e=t= =t=h=y= =s=p=e=e=c=h= =b=e= =s=h=o=r=t=,= =c=o=m=p=r=e=h=e=n=d=i=n=g= =m=u=c=h= =i=n= =f=e=w= =w=o=r=d=s=.

대문자로 변경 : 
LET THY SPEECH BE SHORT, COMPREHENDING MUCH IN FEW WORDS.
'''

print('---quiz8---')
sen = 'Let thy speech be short, comprehending much in few words.'
print('첫번째 t의 위치 :', sen.find('t') + 1)
print('첫번째 m의 위치 :', sen.find('m') + 1)
print('= 으로 연결 : ')
print('='.join(sen))
print('대문자로 변경 : ')
print(sen.upper())
print()

# 퀴즈 9
# 아래와 같이 변수를 지정하고
# humidity = 82
# temperature = -1.8
# % 포맷, format(), f' 포맷 3가지 방식을 이용하여 다음과 같이 출력하여라

'''
오늘의 날씨 : 맑음, 습도 82%, 현재기온 -1.8
'''

print('---quiz9---')
humidity = 82
temperature = -1.8
print('오늘의 날씨 : 맑음, 습도 %d%%, 현재기온 %.1f' % (humidity, temperature))
print('오늘의 날씨 : 맑음, 습도 {}%, 현재기온 {:.1f}'.format(humidity, temperature))
print(f'오늘의 날씨 : 맑음, 습도 {humidity}%, 현재기온 {temperature:.1f}')
