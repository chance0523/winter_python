# chr(), ord() -> 아스키 코드
# all(), any() => True / False
# 유효성 검사 => True / False
# isdigit(), isalpha(), isalnum(), isnumeric(),
# islower(), isupeer(), isdecimal()
# 정렬
# sort(), reverse(), sorted()
# 별도의 Object로 생성 = 다른 함수, lambda 함수에 적용
# zip(), filter(), map()
# dir()

# 내장함수 : 아스키코드와 관련된 함수
# chr(), ord()
# chr(숫자) => 아스키코드값에 해당하는 문자나 숫자
# 문자의 아스키 코드 값을 돌려주는 함수
# 0에서 127 사이의 숫자를 각각 하나의 문자 또는 기호에
# 대응 시켜놓은 코드표
print(chr(65))  # 대문자 'A'는 65
print(chr(97))
print(chr(48))
print(ord('A'))
print(ord('a'))
print(ord('0'))

# 리스트/튜플 등의 원소값이 False 값인지 True 값인지
# all(리스트/튜플/집합) : 값이 모두 True 조건이면 True
# any(리스트/튜플/집합) : 값 중 하나라도 True 조건이면 True
# False 조건값 : None, 0, 0.0, '', False
listA = [0, False, '', ' ']
setB = {0, False, '', None, 0.0}
tupleC = (1, 2, 3, True, 'Yes')
print(any(listA))
print(any(setB))
print(any(tupleC))
print(all(listA))
print(all(setB))
print(all(tupleC))

# 유효성 검사
# 데이터(숫자, 문자 ...)가 조건에 맞는지 검사하는 기능
# 문자열변수.isalpha()
# 모두 문자인가? 숫자문자 제외, True, False
# 문자열변수.isdigit(), 문자열변수.isnumeric()
# 모두 숫자문자인가? True/False
# 문자열변수.isalnum() : 문자열과 숫자로만 구성되어 있는가?
# islower(), isupper() : 대문자/소문자 검사
# isdecimal() : 모두 10진수인가?

str1 = 'fkfkfk'
str2 = '12345'
str3 = '1fdjrgkw435'
str4 = 'BANANA'
print(str1.isalpha())
print(str2.isalpha())
print(str3.isalpha())
print(str1.isdigit())
print(str2.isdigit())
print(str3.isdigit())
print(str1.isalnum())
print(str2.isalnum())
print(str3.isalnum())
print(str4.isupper())
print(str2.isdecimal())


# quiz : 숫자로 구성된 리스트 생성 (길이는 5)
# numList = []
# while True:
#     ip = input('숫자를 입력하세요.')
#     if ip.isdigit():
#         numList.append(ip)
#         if len(numList) == 5:
#             print(numList)
#             break
#     else:
#         print('숫자가 아닙니다.')

def sootsegi(word):
    soot = 0
    for i in word:
        if i.isdigit():
            soot += 1
    print('숫자 갯수 : %d' % soot)
    print('문자 갯수 : %d' % (len(word) - soot))


# quiz : 문자열에서 숫자와 숫자가 아닌 문자의 갯수를 출력하여라
testWord = 'Python1234Java4774'
# soot = 0
# for i in testWord:
#     if i.isdigit():
#         soot += 1
# print('숫자 갯수 : %d' % soot)
# print('문자 갯수 : %d' % (len(testWord) - soot))
sootsegi(testWord)

# 정렬과 관련된 내장함수
# sorted(ㄹ/ㅌ/ㅈ) : 바로 인쇄 가능

# dir(자료형)
# 사용 가능한 속성과 함수를 리스트 구조로 표시
print(dir('String'))
print(dir(True))
print(dir([1, 2, 3, 4, ]))

# zip(리스트1,리스트2)
# zip 객체로 리턴 => for ... in zip 문 이용해서 아이템 확인
# 리스트의 각 아이템 요소를 튜플화 구조로 묶어준다.
# [(아이템1,아이템2) ...]
# zip(*zip객체)
# zip으로 묶어준 객체를 원래대로 풀어준다.
p1 = ['길동', '동미', '미영', '영철']
p1Gender = ['남', '여', '여', '남']
print(zip(p1, p1Gender))
for i in zip(p1, p1Gender):
    print(i)

myList2 = [('a', 'apple'), ('b', 'banana'), ('c', 'cat')]
print(myList2, type(myList2))
x, y = zip(*myList2)
print(x)
print(y)
