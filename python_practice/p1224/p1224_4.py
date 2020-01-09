# 문자열 함수 p.67
# 샘플 문자열 만들기
# http://www.lipsum.com

sampleTxt = '''
et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores
et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia
deserunt mollitia animi, id est laborum et dolorum fuga. Et harum
'''

print('전체 문자열 출력\n', sampleTxt)
print('-' * 30)

# 특정 문자열의 갯수 출력
print('a의 갯수 : ', sampleTxt.count('a'))
print('the의 갯수 : ', sampleTxt.count('the'))

print('-' * 30)

# find : 찾고자하는 문자열이 없으면 -1 반환
# index : 찾고자하는 문자열이 없으면 에러
print('f의 시작위치 =', sampleTxt.find('f'))
print('f의 시작위치 =', sampleTxt.index('f'))
print('가의 시작위치 =', sampleTxt.find('가'))
# print('가의 시작위치 =',sampleTxt.index('가'))

print('-' * 30)

# 대소문자 변환하여 반환
print(sampleTxt.upper())
print(sampleTxt.lower())
print('-' * 30)

print('-' * 30)
# 문자열 교체하기 replace
# et -> was
result = sampleTxt.replace('et', 'was')
print(result)

# join
myWord = 'python'
print(myWord)
print('*'.join(myWord))

# strip : 좌우 공백 제거
mystrip = ' pytorch  '
print(mystrip)
print('*', mystrip.strip(), '*')
print('*', mystrip.lstrip(), '*')
print('*', mystrip.rstrip(), '*')
