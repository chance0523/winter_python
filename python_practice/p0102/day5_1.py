# 교재 참조 - p231 내장 함수 부분

# 함수의 종류
# 사용자정의 함수
# - def 명령으로 함수명 정의
# - lambda 함수 : 익명함수
# 외장함수 : import 외장모듈이나 패키지
#  ex) datetime.now()
# 내장함수 : import 명령없이 사용할 수 있는 함수
#  ex) type(), len()
#    divmod(), min(), max(), abs(), eval()
#   list(), dict(), tuple(), set()
#   int(), float(), str()
#   enumerate()

# char() , ord() => 아스키 코드
# all() , any() => True/False
# 유효성 검사 => True/False
# isdigit(), isalpha(), isalnum(), isnumeric(),
# islower(), isupper(), isdecimal()
# 정렬
# sort(), reverse(), sorted()
# 별도의 Object로 생성 = 다른 함수, lambda 함수에 적용
# zip(), fillter(), map()
# 객체에 대한 속성과 메소드 표시
# dir()

print('-' * 10, '\n' * 2)
# 내장함수 : 아스키코드와 관련된 함수
# char() , ord()
# char(숫자) => 아스키코드값에 해당하는 문자나 숫자
# 문자의 아스키 코드 값을 돌려주는 함수
# 0에서 127 사이의 숫자를 각각 하나의 문자 또는 기호에
# ord(관련 문자나 숫자) => 아스키코드값
# char()과 반대되는 함수
# 대응시켜 놓은 코드표
# https://ko.wikipedia.org/wiki/ASCII
print(chr(65))  # 'A'
print(chr(97))  # 'a'
print(chr(48))  # '0'
print(ord('A'))  # 65
print(ord('a'))  # 97
print(ord('0'))  # 48
print('-' * 10, '\n' * 2)

# 리스트/튜플 등의 원소값이 False 값인지 True 값인지
# Boolean 형(True/False)로 표시
# all(리스트/튜플/집합) :  값이 모두 True 조건이면 True
# any(리스트/튜플/집합) : 값중 하나라도 True 조건이면 True
# False 조건값 : None, 0, 0.0, '', False
listA = [0, False, '', ' ']
setB = {0, False, '', None, 0.0}
tupleC = (1, 2, 3, True, 'Yes')
print(any(listA))  # True
print(any(setB))  # False
print(any(tupleC))  # True
print(all(listA))  # False
print(all(setB))  # False
print(all(tupleC))  # True

print('-' * 10, '\n' * 2)

# 유효성 검사?
# 데이터(숫자, 문자...)가 조건에 맞는지 검사하는 기능
# 문자열변수.isalpha()
# : 모두 문자(알파벳,한글..)인가? 숫자문자제외 , True/Fasle
# 문자열변수.isdigit() , 문자열변수.isnumeric()
# : 모두 숫자문자인가?  , True/Fasle
# 문자열변수.isalnum() : 문자열과 숫자로만 구성되어 있는가?
# islower(), isupper() : 대문자/ 소문자 검사
# isdecimal() : 모두 10진수인가?
str1 = 'fkfkfk'
str2 = '12345'
str3 = '1fdkjfsl2345'
str4 = 'BANANA'
str5 = '#&^=+'
print(str1.isalpha())  # True
print(str2.isalpha())  # False
print(str3.isdigit())  # False
print(str1.isdigit())  # False
print(str2.isdigit())  # True
print(str3.isalnum())  # True
print(str4.isupper())  # True
print(str1.islower())  # True
print(str2.isdecimal())  # True
print(str3.isdecimal())  # False
print(str5.isalpha())  # False
print('-' * 10, '\n' * 2)

# 퀴즈 : 숫자로 구성된 리스트 생성 (길이는 5)
# 빈 리스트를 생성한다.
# 입력문이 실행된다.
# 입력값이 숫자이면 리스트에 추가한다.
# 입력값이 숫자가 아니면 다시 입력문이 실행된다.
# 리스트의 전체길이가 5이면 입력을 종료한다.
# 리스트를 출력한다.

# # 결과값을 저장할 빈 리스트 생성
# resultList = []
# # 입력값을 받을 수 있게 while 문 생성
# while True:
#     data = input('데이타를 입력해주세요?....')
#     # 숫자이면 리스트 추가 => 유효성 검사
#     if data.isdigit():
#         resultList.append(data)
#         print('리스트가 추가되었습니다.')
#     else:
#         print('숫자가 아닙니다. 다시 입력해주세요 ')
#     # 탈출 조건
#     if len(resultList) == 5:
#         break
# # 리스트 출력
# print(resultList)

# 퀴즈 : 문자열에서 숫자와 숫자가아닌문자의 갯수를 출력하여라
# testWord = 'Python1234Java4774'
'''
결과 >>
숫자 갯수 : ? 
문자 갯수 : ?
'''


# 문자열변수 정의
# 숫자갯수를 저장할 변수 정의 : cnt
# 반복문 생성 : 문자열에서 숫자라면 : cnt += 1 값을 증가시킨다.
# 숫자갯수 출력
# 문자갯수는? len(문자열변수)-cnt
# testWord = 'Python1234Java4774'
# cnt = 0 # 숫자갯수를 저장할 변수
# for i in testWord:
#     if i.isdigit():
#         cnt += 1
# print( '숫자갯수 : ', cnt)
# print( '문자갯수 : ', len(testWord)-cnt)

# 사용자 정의 함수로 변경
def checkStringCount(word):
    cnt = 0  # 숫자갯수를 저장할 변수
    for i in word:
        if i.isdigit():
            cnt += 1
    print('\nword : ', word)
    print('숫자갯수 : ', cnt)
    print('문자갯수 : ', len(word) - cnt)


checkStringCount('Python1234Java4774')
checkStringCount('가나다라1234')
'''
word :  Python1234Java4774
숫자갯수 :  8
문자갯수 :  10

word :  가나다라1234
숫자갯수 :  4
문자갯수 :  4
'''

print('-' * 10, '\n' * 2)
# 정렬과 관련된 내장 함수
# sorted(리스트/튜플/집합..)
# : 바로 인쇄 가능. 튜플과 집합은 정렬된 형태의 리스트로 변경
# : 데이타 정렬
# : 결과값을 리턴한다. => print()로 바로 출력
# 리스트이름.sort() : 리스트정렬
# 리스트이름.reverse() : 리스트 역정렬

myList = ['b', 'a', 'c', 'x']
myTuple = ('b', 'a', 'c', 'x')
mySet = {'b', 'a', 'c', 'x'}
print(myList.sort())  # None
myList.sort()
# 오류 발생 : AttributeError
# myTuple.sort()
print(myList)  # ['a', 'b', 'c', 'x']
myList.reverse()
print(myList)  # ['x', 'c', 'b', 'a']
# 바로 출력 가능
print(sorted(['b', 'a', 'c', 'x']))  # ['a', 'b', 'c', 'x']
print(sorted(myTuple))  # ['a', 'b', 'c', 'x']
print(sorted(mySet))  # ['a', 'b', 'c', 'x']

print('-' * 10, '\n' * 2)

# ---------- #
# dir(자료형) => Reference 기능
# 사용가능한 속성과 함수를 리스트 구조로 표시
print(dir('String'))
print(dir(True))
print(dir(100))
print(dir([1, 2, 3, 4, 5]))
print(dir((1, 2, 3, 4, 5)))
print(dir({1: '하나', 2: '둘'}))
print(dir({1, 2, 3, 4, 5}))
print('-' * 10, '\n' * 2)

'''
['__add__', '__class__', '__contains__', 
'__delattr__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__',
  '__getitem__', '__getnewargs__', '__gt__', 
  '__hash__', '__init__', '__init_subclass__',
   '__iter__', '__le__', '__len__', '__lt__', 
   '__mod__', '__mul__', '__ne__', '__new__', 
   '__reduce__', '__reduce_ex__', '__repr__', 
   '__rmod__', '__rmul__', '__setattr__', 
   '__sizeof__', '__str__', '__subclasshook__',
    'capitalize', 'casefold', 'center', 'count',
     'encode', 'endswith', 'expandtabs', 
     'find', 'format', 
     'format_map', 'index', 
     'isalnum', 'isalpha', 'isascii', 
     'isdecimal', 'isdigit', 'isidentifier',
      'islower', 'isnumeric', 'isprintable', 
      'isspace', 'istitle', 'isupper', 'join', 
      'ljust', 'lower', 'lstrip', 'maketrans', 
      'partition', 'replace', 'rfind', 'rindex', 
      'rjust', 'rpartition', 'rsplit', 'rstrip', 
      'split', 'splitlines', 'startswith', 'strip',
       'swapcase', 'title', 'translate', 'upper', 
       'zfill']

'''

# ---------- #
# zip(리스트1, 리스트2 .. )
# zip 객체로 리턴 => for...in zip 문 이용해서 아이템 확인
# : 리스트의 각 아이템요소를 튜플화 구조로 묶어준다.
# list(zip 객체): [(아이템1,아이템2) ...]
# zip(*zip객체)
# : zip으로 묶어준 객체를 원래대로 풀어준다.

p1 = ['길동', '동미', '미영', '영철']
p1Gender = ['남', '여', '여', '남']
# zip 객체로 출력
print(zip(p1, p1Gender))
# 하나씩 출력
for i in zip(p1, p1Gender):
    print(i)
# 각각 구분자로 분리해서 출력
for i, j in zip(p1, p1Gender):
    print(i, '-', j)
# 리스트화
print(list(zip(p1, p1Gender)))
# [('길동', '남'), ('동미', '여'), ('미영', '여'), ('영철', '남')]

# zip으로 리스트안의 튜플구조 해제하기 - unzip
# 변수1, 변수2 = zip(*리스트튜플이름)
# 결과물은 같은 인덱스의 값만 튜플로 다시 생성
# 리스트 튜플 정의
myList2 = [('a', 'apple'), ('b', 'banana'), ('c', 'cat')]
print(myList2, type(myList2))
x, y = zip(*myList2)
print(x)  # ('a', 'b', 'c')
print(y)  # ('apple', 'banana', 'cat')

print('-' * 10, '\n' * 2)

# 딕셔너리 구조를 튜플 형태로 변경
# 딕셔너리  => 키 리스트, 값 리스트 => zip =>  unzip 튜플
myDict = {'a': 'africa', 'd': 'drama', 'm': 'movie'}
print(f'myDict = {myDict}, {type(myDict)}')
# 키 조합으로 리스트 생성
print(list(myDict))
# 값만 조합으로 리스트 생성
print(list(myDict.values()))
# zip 객체로 변경한 후 하나씩 출력
print(zip(list(myDict), list(myDict.values())))
for i in zip(list(myDict), list(myDict.values())):
    print(i)
# zip 객체의 리스트화 => 리스트 튜플
print(list(zip(list(myDict), list(myDict.values()))))
# unzip => 튜플
x, y = zip(*zip(list(myDict), list(myDict.values())))
print(x)
print(y)
'''
myDict = {'a': 'africa', 'd': 'drama', 'm': 'movie'}, <class 'dict'>
['a', 'd', 'm']
['africa', 'drama', 'movie']
<zip object at 0x02FC3228>
('a', 'africa')
('d', 'drama')
('m', 'movie')
[('a', 'africa'), ('d', 'drama'), ('m', 'movie')]
('a', 'd', 'm')
('africa', 'drama', 'movie')
'''

print('-' * 10, '\n' * 2)

# ---------- #
# filter(함수명/lambda 함수, 리스트/튜플),
# map(함수명/lambda 함수, 리스트/튜플),
# reduce(함수명/lambda 함수, 리스트/튜플)
# 정의된 사용자정의함수, 람다함수를
# 리스트 데이타 각각에 적용한다.

# filter()
# filter(함수명/lambda 함수, 리스트/튜플)
# 사용할 함수는 결과값이 True/False
# 함수를 적용하여 리스트/튜플의 data에서 True 인것만 Return
# => 참인조건의 리스트만 출력

print('퀴즈:리스트 중 짝수만 출력하기 ')


# 퀴즈
# 리스트 중 짝수만 출력하기 = filter() 함수 이용
# 짝수인지 판독하는 함수 정의
# 리스트 정의
# filter() 함수 적용 => filter 객체
# filter 객체를 리스트화

# filter()를 사용하지 않은 경우 일반 함수 적용
def oddPrint(list):
    resultList = []
    for i in list:
        if i % 2 == 0:
            resultList.append(i)
    return resultList


print(f'짝수만 출력(일반함수) : {oddPrint([10, 30, 5, 9, 18])} ')
# 짝수만 출력 : [10, 30, 18]
print('짝수만 출력(filter() 함수)')


# filter 함수에 사용할 함수 정의
# 리스트 각각의 요소에 적용할 함수
# 결과값은 True / False
def oddPrint2(n):
    if n % 2 == 0:
        return True


print(oddPrint2(10))  # True
print(filter(oddPrint2, [10, 30, 5, 9, 18]))  # filter object at 0x000001D5879C69E8>
for i in filter(oddPrint2, [10, 30, 5, 9, 18]):
    print(i)
'''
10
30
18
'''
print(list(filter(oddPrint2, [10, 30, 5, 9, 18])))
# [10, 30, 18]

print('짝수만 출력(filter()와 lambda 함수)')
# 함수변수 = lambda 인자:명령
# 함수변수(인자)
f_odd = lambda x: x % 2 == 0
print('람다 호출 = ', f_odd(40))  # True
# filter(lambda 인자:명령, 적용할데이타리스트) => filter객체
print(filter(lambda x: x % 2 == 0, [10, 30, 5, 9, 18]))  # <filter object at 0x0000022A90FB69E8>
print(list(filter(lambda x: x % 2 == 0, [10, 30, 5, 9, 18])))
# [10, 30, 18]
for i in filter(lambda x: x % 2 == 0, [10, 30, 5, 9, 18]):
    print(i)

'''
10
30
18
'''

print('\n퀴즈:숫자 리스트에서 양수만 출력하기 ')
numlist = [10, -30, 20, 5, -100]
# 양수인지 판독하는 함수 정의
print('양수만 출력(일반 함수)')


def positive_num(list):
    result = []
    for i in list:
        if i > 0:
            result.append(i)
    return result


print(positive_num(numlist))
# [10, 20, 5]

print('양수만 출력(filter() 함수)')


def positive(n):
    return n > 0


print(positive(-10))  # False
print(positive(10))  # True
# filter() 함수 적용
print(filter(positive, numlist))  # <filter object at 0x01DAFB30>
# 리스트화 : 양수만 추출
print(list(filter(positive, numlist)))  # [10, 20, 5]
# for .. in 으로 출력
for i in filter(positive, numlist):
    print(i)
'''
10
20
5
'''

print('양수만 출력(filter(), lambda 함수)')
f_positive = lambda x: x > 0
print(f_positive(-7))  # False
print(f_positive(7))  # True
print(list(filter(lambda x: x > 0, numlist)))
for i in filter(lambda x: x > 0, numlist):
    print(i)
'''
[10, 20, 5]
10
20
5
'''

print('\n퀴즈:문자열에서 숫자만 리스트로 만들기  ')
message = 'ab4690cfvg342가1나1다0'
print('숫자만 출력(일반 함수)')


def numList(txt):
    result = []
    for i in range(0, len(txt)):
        if txt[i].isdigit():
            result.append(txt[i])
    return result


print(numList(message))
# ['4', '6', '9', '0', '3', '4', '2', '1', '1', '0']
# 위의 일반 함수를 filter(함수명, 리스트) 와
# filter(lambda 함수정의, 리스트) 형태로 변경하여 보세요
# 문자열을 리스트로 변경하기
# 문자 사이에 공백 삽입하기 : ' '.join(문자열변수)
print(' '.join(message))
# 문자열에서 공백을 기준으로 리스트 생성
# 문자열.split()
print(' '.join(message).split())
# a b 4 6 9 0 c f v g 3 4 2 가 1 나 1 다 0
# ['a', 'b', '4', '6', '9', '0', 'c', 'f', 'v', 'g', '3', '4', '2', '가', '1', '나', '1', '다', '0']
messageList = ' '.join(message).split()
print('숫자만 출력(filter() 함수)')


def digitPrint(c):
    return c.isdigit()


print(list(filter(digitPrint, messageList)))
# ['4', '6', '9', '0', '3', '4', '2', '1', '1', '0']
print('숫자만 출력(filter(), lambda 함수)')
print(list(filter(lambda x: x.isdigit(), messageList)))
# ['4', '6', '9', '0', '3', '4', '2', '1', '1', '0']
