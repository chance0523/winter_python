# 현재 작업폴더 위치 확인하기
# python.exe 위치 , 현재 파이썬 파일 정보 출력

# 파일입출력
# 파일변수  = open(파일경로, 'r'/'w'/'a', encoding='utf-8/cp949')
# 파일변수.파일입출력함수(옵션)

# 파일읽기함수
# read() : 파일전체 문자열 구조
# readline() : 파일에서 첫줄만 읽기
# readlines() : 각행이 리스트 구조로 변경

# 파일 닫기 - 명령실행 뒤에 배치
# 파일변수.close()

# ----------------
# 파일 읽기 1 - read()
# 파일변수 = open('파일경로', 'r')
# 파일전체 문자열데이터로 리턴
# 문자열변수 = 파일변수.read()


# 문서는 몇개의 단어로 구성되어 있을까?
# 단어별로 구성해서 리스트 구조로 변경
# 문자열변수.split() => 공백기준으로 리스트로 변경


# 퀴즈
# 파일의 단어전체수와 3개의 단어가
# 표시되는 함수를 정의하여라
'''
>> 함수호출
printWord('data/sample.txt')
printWord('data/Yesterday.txt')

>> 결과값 
파일명 : data/sample.txt
단어 갯수 : 134
단어 3개 출력 
['Yesterday', 'All', 'my']
'''

# 퀴즈 :
# 파일을 읽은 후 파일명과 10개의 단어만 출력한 후
# 단어의 갯수를 출력하는 함수를 작성하여라
'''
# 함수 호출 
fileread('data/Yesterday.txt')
fileread('data/sample.txt')

파일명 :  data/Yesterday.txt
['Yesterday', 'All', 'my', 'troubles', 'seemed', 'so', 'far', 'away', 'Now', 'it']
단어 갯수 :  134
******************************
파일명 :  data/sample.txt
['Yes는', '사랑과', '자유에', '대한', '긍정적인', '태도를', '의미하는', '것이다.', '오늘부터라도', '당신의']
단어 갯수 :  1299

'''

print('퀴즈 : 파일읽은 후 출력하기 ')

# ----------------
# 파일 읽기 2 - 첫줄만 readline()
# 파일변수 = open('파일경로', 'r')
# 첫번째 줄만 출력하기 -> 문자열
# 문자열변수 = 파일변수.readline()


# ----------------
# 파일 읽기 3 - readlines()
# 파일변수 = open('파일경로', 'r')
# 한줄씩 읽어서 리스트 요소로 저장
# 리스트이름 = 파일변수.readlines()


# # 퀴즈
# '''
#   샘플텍스트파일의 행수가 몇개인지 출력하여라
# '''
#
'''
# 함수호출 
lineRead('data/sample.txt')
lineRead('data/Yesterday.txt')

결과>>
파일명 :  data/sample.txt
행 수 :  245
******************************
파일명 :  data/Yesterday.txt
행 수 :  30

'''
print('\n\n 퀴즈 : 파일의 행수는 몇개일까요?')

#
# 퀴즈
# data.txt 파일안의 데이타의 합과 평균을 구하는
# 함수를 정의하고 아래와 같이 출력하여라
'''
# 함수 호출 
sumAvr('data/data_eng.txt')
sumAvr('data/data_kor.txt')

>> 결과

파일명 =  data/data_eng.txt
데이터 수 =  12
합 =  933
평균 = 77.75

----------
파일명 =  data/data_kor.txt
데이터 수 =  12
합 =  892
평균 = 74.33

'''

# -------------------------
# 문자열 함수 활용
# 공백과 개행 없애기
# 문자열변수.replace('\n','')
# 문자열변수.replace(' ,'')

print('-' * 10, '\n\n')
# 공백과 개행 그대로 파일읽은 후 글자수 출력하기


# 공백과 개행 삭제한 후 글자수 출력하기
