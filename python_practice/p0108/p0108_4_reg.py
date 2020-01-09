# 정규표현식 (Regular Expression)
# 유효성 검사
# 특정 문자열이 특정 조건(패턴)에 맞는지 검사

# 파이썬에서 정규표현식 모듈 => re (내장모듈)
import re

# print(dir(re))

# ------------------------------------
# 방식 1
# 패턴변수 = re.compile(패턴식)
# 패턴변수.정규표현식메소드(문자열)
# 정규표현식 메소드
# match(문자열) : 문자열 처음부터 검색 => 문자열 / None
# search(문자열) : 문자열 전체 검색 => 문자열 / None
# findall(문자열) : 정규식과 매치되는 문자열을 리스트로 반환 => 리스트 / []
# finditer(문자열) : 정규식과 매치되는 문자열을 반복가능한 객체로 반환 => iterator 객체 / None

pattern1 = re.compile('^ab')  # ab로 시작하는
print(pattern1.findall('above'))  # ['ab']
print(pattern1.findall('dread'))  # []
print(pattern1.match('address'))  # None
print(pattern1.search('above'))  # <re.Match object; span=(0, 2), match='ab'>
print(pattern1.finditer('above'))  # <callable_iterator object at 0x000001676375B7C0>

obj1 = pattern1.finditer('above')
obj2 = pattern1.finditer('word')
for i in obj1:
    print(i)
for i in obj2:
    print(i)

# ------------------------------------
# 방식 2
# 문자열변수 = 문자열값
# re.정규표현식메소드(패턴식, 문자열변수)
# re.match(패턴식, 문자열변수) => 문자열
# re.search(패턴식, 문자열변수) => 문자열
# re.findall(패턴식, 문자열변수) => 리스트
# re.finditer(패턴식, 문자열변수) => 반복가능객체

# 정규표현식 패턴 - 대문자, 소문자, 숫자, 한글
# [문자클래스스타일]  => 한글자씩
# [문자클래스스타일]+ => 단어단위
# [a-z] : 영어소문자
# [A-Z] : 영어대문자
# [0-9] : 숫자
# [가-힣] : 한글

# Match object 메서드
# group() : 매치된 문자열을 리턴한다.
# start() : 매치된 문자열의 시작 위치를 돌려준다.
# end() : 매치된 문자열의 끝 위치를 돌려준다.
# span() : 매치된 문자열의 시작,끝 위치를 튜플 형태로 돌려준다.

txt1 = "가나다 009 Python ?### 7834 파이썬 MYSQL"
print(re.findall('[가-힣]', txt1))  # ['가', '나', '다', '파', '이', '썬']
print(re.findall('[가-힣]+', txt1))  # ['가나다', '파이썬']
print(re.findall('[a-z]', txt1))  # ['y', 't', 'h', 'o', 'n']
print(re.findall('[a-z]+', txt1))  # ['ython']
print(re.findall('[A-Z]+', txt1))  # ['P', 'MYSQL']
print(re.findall('[0-9]+', txt1))  # ['009', '7834']
print(re.findall('[a-zA-Z]+', txt1))  # ['Python', 'MYSQL']
for i in re.finditer('[a-zA-Z]+', txt1):
    print(i)
    print(i.group())
    print(i.span())
    print(i.start())
    print(i.end())
    print()
    # <re.Match object; span=(8, 14), match='Python'>
    # Python
    # (8, 14)
    # 8
    # 14

# 정규표현식 패턴 - 대문자, 소문자, 숫자 : \지원문자
# [\d] : 10진수, [0-9]와같음
# [\D]: 10진수외 [^0-9]
# [\s] :공백문자, [ \t\n\r\f\v]
# [\S]: 공백 문자 외, [ \t\n\r\f\v]
# [\w] : 영문자숫자 , [a-zA-Z0-9]
# [\W]: 영문자숫자외 , [^a-zA-Z0-9]

txt2 = '''
        가나나 $ 009 Python ?#
        7834 파이썬 java WORD _+
        784 ENGLISH
'''
print(re.findall('[\d]', txt2))
print(re.findall('[\S]', txt2))
print(re.findall('[\w]', txt2))
print(re.findall('[\W]', txt2))
# ['0', '0', '9', '7', '8', '3', '4', '7', '8', '4']
# ['가', '나', '나', '$', '0', '0', '9', 'P', 'y', 't', 'h', 'o', 'n', '?', '#', '7', '8', '3', '4', '파', '이', '썬', 'j', 'a', 'v', 'a', 'W', 'O', 'R', 'D', '_', '+', '7', '8', '4', 'E', 'N', 'G', 'L', 'I', 'S', 'H']
# ['가', '나', '나', '0', '0', '9', 'P', 'y', 't', 'h', 'o', 'n', '7', '8', '3', '4', '파', '이', '썬', 'j', 'a', 'v', 'a', 'W', 'O', 'R', 'D', '_', '7', '8', '4', 'E', 'N', 'G', 'L', 'I', 'S', 'H']
# ['\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '$', ' ', ' ', ' ', '?', '#', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '+', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\n']

print(re.findall('[\d]+', txt2))
print(re.findall('[\S]+', txt2))
print(re.findall('[\w]+', txt2))
print(re.findall('[\W]+', txt2))


# ['009', '7834', '784']
# ['가나나', '$', '009', 'Python', '?#', '7834', '파이썬', 'java', 'WORD', '_+', '784', 'ENGLISH']
# ['가나나', '009', 'Python', '7834', '파이썬', 'java', 'WORD', '_', '784', 'ENGLISH']
# ['\n        ', ' $ ', ' ', ' ?#\n        ', ' ', ' ', ' ', ' ', '+\n        ', ' ', '\n']

# 비밀번호 유효성 검사
# 비밀번호 조건
# 전체길이는 6~12
# 영어 대소문자, 숫자만
# checkPwd('abcd') => 길이문제
# checkPwd('abcd+가나다') => 문자문제

def checkPwd(pwd):
    pattern = re.compile('[a-zA-Z0-9]')
    print(pattern.findall(pwd))
    if len(pwd) < 6 or len(pwd) > 12:
        return '길이는 6~12 글자여야 합니다'
    elif pwd == pattern.match(pwd).group():
        return '완벽합니다'
    else:
        return '영어 대소문자와 숫자만 가능합니다'


print(checkPwd('abcd'))
print(checkPwd('abcdgrdgsn'))
print(checkPwd('abcd+가나다'))
print(checkPwd('abcd123gogo'))

# 자릿수 지정 패턴 {}
# [문자열]{n} n번 반복됨
# [문자열]{n,} n번 이상 반복됨
# [문자열]{n, m} 최소 n번 이상 최대 m번 이하로 반복됨
# x* : 문자열 X가 0번이상 반복

print('-' * 30)
str = "abc 00ab 000abcd 00000abcd 00000000abcd"
print(re.findall('[0]{2}[a-bA-B]+', str))
print(re.findall('[0]{2,}[a-bA-B]+', str))
print(re.findall('[0]{0,3}[a-bA-B]+', str))

# 정규표현식 컴파일 옵션
# re.compile(정규표현식, re.컴파일옵션)
# S : dotall 줄바꿈문자 포함
# I : ignorecase  대소문자 관계없이 매치
# M : multiline 여러줄과 매치한다
# v : verbose 모드 이용. 여러줄 정규식과 주석 사용 가능


# 정규표현식 메타문자
# | : OR 또는
# +:바로 앞의 문자가 하나 이상 있음
# ^:문자열의 처음을 나타냄
# $:문자열의 끝
# . :임의의 문자가 와도 됨
# *:바로 앞의 문자가 없거나 하나 이상 있음
# ?:앞의 문자가 없거나 하나임

# 휴대폰번호 유효성 검사
# 3자리 - 4자리 - 4자리
txt2 = '''010-7777-1234 00-6785-가나다 010-58-ab-r 045-4488-1122016-8456-1378
            017-7484-9231 031-441-3658 011-6258-7413 01048441335'''
# print(re.findall('[0-9]{3}-[0-9]{4}-[0-9]{4}', txt2)) # 숫자 3자리 - 숫자 4자리 - 숫자 4자리만 검사
# ['010-7777-1234', '045-4488-1122', '016-8456-1378', '017-7484-9231']
print(re.findall('01[0|1|6|7]-[0-9]{4}-[0-9]{4}', txt2))  # 숫자 3자리(010/011/016/017) - 숫자 4자리 - 숫자 4자리 검자

# 입력받은 번호가 모바일폰 형식이면 메세지 출력
# userPhone = input('핸드폰 번호를 입력해주세요. (예 : 000-0000-0000) ')
# mobilePattern = '01[0|1|6|7]-[0-9]{4}-[0-9]{4}'
# print(re.search(mobilePattern, userPhone))
# print(re.search(mobilePattern, userPhone).group())

# quiz
# 주민등록번호 유효성 검사
# userID = input('주민 등록 번호를 입력해주세요. (예 : 000000-0000000) ')
# juminPattern = '[0-9]{6}-[1|2|3|4][0-9]{6}'
# print(re.search(juminPattern, userID))
# print(re.search(juminPattern, userID).group())

# 그루핑 이용
# 정규표현식의 패턴을 그룹화 : group(index)
juminPattern = '([0-9]{6})-([1|2|3|4][0-9]{6})'
result = re.match(juminPattern, '123456-1234567')
print(result)  # <re.Match object; span=(0, 14), match='123456-1234567'>
print(result.group())  # 123456-1234567
print(result.group(1))  # 123456
print(result.group(2))  # 1234567

# quiz
# 주민번호 데이터에서 뒷자리는 '*******' 로 변경
quizList = ['940516-1465284', '840516-2158468', '510514-1054786', '540718-1047894']
juminPattern = '([0-9]{6})-([1|2|3|4][0-9]{6})'
for i in quizList:
    result = re.match(juminPattern, i)
    print(f'{result.group(1)}-{"*******"}')
