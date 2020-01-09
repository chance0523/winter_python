# in / not in 연산자
# 아이템 in 그룹 (튜플, 리스트, 문자열, 집합) => True, False
# 아이템 not in 그룹 (튜플, 리스트, 문자열, 집합) => True, False

# 문자가 문자열에 있는가?
print('a' in 'banana')  # True
print('a' in 'Python')  # False
print('a' not in 'Python')  # True

# 값이 리스트에 있는가?
myList = [100, 200, 300]
print(100 in myList)  # T
print(1 in myList)  # F
print(1 not in myList)  # T

singer1 = '지민'
singer2 = '카이'
bts = ['지민', 'RM', '슈가', '진', '정국', '뷔', '제이홉']
if singer1 in bts:
    print('{} : bts 멤버이다.'.format(singer1))
if singer2 not in bts:
    print('{} : bts 멤버가 아니다.'.format(singer2))

myClass = {'python', 'c', 'java', 'c++'}
print(myClass, type(myClass))
if '어셈블리' not in myClass:
    print('어셈블리 미수강')
if 'python' not in myClass:
    print('python 미수강')
else:
    print('python 수강')

t1 = ('바나나', '포도', '수박', '자두')
if '체리' in t1:
    print('바나나가 우리집 냉장고에 있다')
elif '포도' in t1:
    print('포도가 많이 우리집 냉장고에 있다')
else:
    print('냉장고에 과일이 없다')
