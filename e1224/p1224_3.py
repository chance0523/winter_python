# indexing & slicing
sen = "Life is too short"
print('sen[3] = ', sen[3])
print('sen[:3] = ', sen[:3])
print('sen[-1] = ', sen[-1])
print('sen[::] = ', sen[::])
print('sen[::2] = ', sen[::2])
print('sen[2::2] = ', sen[2::2])
print('sen[2:11:2] = ', sen[2:11:2])
print('sen[-1:] = ', sen[-1:])
print('sen[-5:-1] = ', sen[-5:-1])

print('len(sen) = ', len(sen))
print('len(sen[:3]) = ', len(sen[:3]))
print('len(sen[-1]) = ', len(sen[-1]))

print('sen[:4], sen[-5:] = ', sen[:4], sen[-5:])

# formatting
# %를 이용한 formatting
# format()를 이용한 formatting
# f'를 이용한 formatting. python version 3.6 ++
today = '화요일'
yesterday = '수요일'
# 오늘은 화요일입니다.
print('오늘은', today, '입니다.')
print('오늘은 %s입니다.' % today)
print('오늘은 %s입니다. 내일은 %s입니다.' % (today, yesterday))

myNum = 16
print('10진수 : %d' % myNum)
print('16진수 : %x' % myNum)
print('8진수 : %o' % myNum)
print('실수 : %f' % myNum)
print('소숫점 두자리 : %.2f' % myNum)

pi = 3.141592
print('pi : %f' % pi)
print('pi : %.3f' % pi)
print('pi : %10.2f' % pi)
print('pi : %3.5f' % pi)
print('pi : %15.1f' % pi)

print('\n' * 5)
# quiz
# 두개의 숫자를 입력받아 다음과 같이 출력하여라
'''
print('-'*20)
print('\t\tquiz')
print('-'*20)
a1 = input('숫자1을 입력하세요...')
a2 = input('숫자2를 입력하세요...')

a1=int(a1)
a2=float(a2)

print('입력받은 숫자1은 %d입니다.' % a1)
print('입력받은 숫자1은 8진수로 %o입니다.' % a1)
print('입력받은 숫자1은 16진수로 %x입니다.' % a1)
print('입력받은 숫자2는 %.1f입니다.' % a2)
'''

todayM = 0.0005
# print('오늘의 미세먼지 농도는 %f%입니다.'%todayM) <- TypeError 발생
print('오늘의 미세먼지 농도는 %f%%입니다.' % todayM)

userName = '홍길동'
userNumber = 123.45
print('user Name : %10s ** ' % userName)
print('user Name : %-10s ** ' % userName)
print('user Name : %10d ** ' % userNumber)
print('user Name : %-15f ** ' % userNumber)

print('\n' * 5)
'''
format을 이용한 출력방식
'문자열1 {} {}'.format(변수1, 변수2)
'문자열1 {숫자나 변수} {숫자나 변수} 문자열2'.format(변수1, 변수2)
'''

color = 'blue'
myNumber = 7

print('color {} number {}'.format(color, myNumber))

# index
print('순서 교체 : number {1} color {0}'.format(color, myNumber))

# 초기값 다시 지정
print('이름지정 : number {myNumber} color {color}'.format(myNumber=100, color='red'))

# 여백
print('-----------------')
print('... {} ...'.format('hello world'))
print('... {:>30} ...'.format('hello world'))
print('... {:<30} ...'.format('hello world'))
print('... {:^30} ...'.format('hello world'))
print('... {:*>30} ...'.format('hello world'))
print('... {:*<30} ...'.format('hello world'))

print('----------------')
pi2 = 3.141592
print('pi : ', format(pi2))
print('pi : ', format(pi2, '11.3f'))
print('pi : {0:2.1f}'.format(pi2))

print('-' * 20)
fruit = "사과, 바나나, 홍시"
print("{} {{...}}".format(fruit))

# f string formatting : version 3.6 ++
# f' 문자열 {변수명이나 변수를 이용한 수식}
print('-' * 20)
stName1 = '나은'
stName2 = '건후'
age = 10
print(f'학생1 {stName1} 학생2 {stName2}')
print('학생1 {} 학생2 {}'.format(stName1, stName2))
print(f'나이1 {age}, 나이2 {age + 5}')

height = 155.67890
print(f'키는? {height}')
print(f'키는? {height:.2f}')
print(f'키는? {height:10.1f}')

print('-'*20)
message='Hello World'
print(f' *** {message:>30} ***')
print(f' *** {message:<30} ***')
print(f' *** {message:^30} ***')
print(f' *** {message:#^30} ***')