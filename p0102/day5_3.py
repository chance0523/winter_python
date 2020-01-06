# 교재 p171
# 하위 폴더 data 확인

# 현재 작업폴더 위치 확인하기
# python.exe 위치 , 현재 파이썬 파일 정보 출력
import os
print(os.getcwd())


# 파일입출력
# 파일변수  = open(파일경로, 'r'/'w'/'a',
#                    encoding='utf-8/cp949')
# 파일변수.파일입출력함수(옵션)

# 파일읽기
# 파일변수 생성
# 파일변수  = open(파일경로, 'r',
#                     encoding='utf-8/cp949')
# 파일변수.read() : 파일전체 문자열 구조 =>  문자열
# 파일변수.readline() : 파일에서 첫줄만 읽기 => 문자열
# 파일변수.readlines() : 각행이 리스트 구조로 변경 => 리스트

# ------------
# 문서 읽기1 - 파일변수.read()
f = open('data/Yesterday.txt', 'r')
print(f)
#  io 객체 출력 - 파일의 인코딩과 경로 확인
#  파일경로가 올바르지 않으면 FileNotFoundError
# 문서 전체가 출력
data = f.read()
print(data, '\n\n',type(data))
# <class 'str'> 문자열
# 첫글자만 추출
print(f'첫 글자 => {data[0]}') # 첫 글자 => Y
# 10글자만 추출
print(f'10글자만 추출 => {data[0:10]}')
# 10글자만 추출 => Yesterday

# 문서는 몇개의 어구로 구성되어 있을까?
# 단어별로 구성해서 리스트 구조로 변경
# 문자열변수.split() => 공백기준으로 리스트로 변경
dataList = data.split()
# 3개만 출력
print(type(dataList))
print(dataList[:3])
print('단어 수? => ', len(dataList) )
'''
['Yesterday', 'All', 'my']
단어 수? =>  134
'''
# 파일 닫기 : 파일변수.close()
f.close()
# ------------
# 문서 읽기2 - 파일변수.readline()
# 파일변수 = open('파일경로', 'r')
# 첫번째 줄만 출력하기 -> 문자열
# 변수 = 파일변수.readline()

f = open('data/sample.txt','r')
data2 = f.readline()
print('\n\n 첫줄만 출력 : \n\n' , data2, '\n',type(data2))
f.close()

# # ----------------
# 파일 읽기 3 - readlines()
# 파일변수 = open('파일경로', 'r', encoding='utf-8/cp949')
# 한줄씩 읽어서 리스트 요소로 저장
# 리스트이름 = 파일변수.readlines()
f = open('data/sample.txt','r')
data3 = f.readlines()
print('\n 전체 출력 : \n\n' , data3, '\n',type(data3))
# 3개의 요소만 출력
print(data3[0:3],'\n\n', type(data3))
# 리스트 요소 단위로 5줄만 출력하기
for i in data3[0:5]:
    print(i)
# 파일닫기
f.close()

#-------------
# 퀴즈
# 파일의 단어전체수와 3개의 단어가
# 표시되는 함수를 정의하여라
'''
def printWord(fileURL, op):
    #명령어 기입 
'''
# >> 함수호출
# printWord('data/Yesterday.txt')
# >> 결과값
# 파일명 : data/Yesterday.txt
# 단어 갯수 : 134
# 단어 3개 출력
# ['Yesterday', 'All', 'my']


print('퀴즈 : 파일의 단어전체수와 3개의 단어만 출력하기 ')
def printWord(fileUrl, op):
    f = open(fileUrl,'r', encoding=op)
    data = f.read()
    myList = data.split()
    print('*'*30)
    print('파일명 : ', fileUrl)
    print( '단어 갯수 : ',len(myList) )
    print( '단어 3개 출력' )
    print(myList[0:3])
    f.close()

printWord('data/Yesterday.txt', 'cp949')
printWord('data/color.txt', 'utf-8')
'''
퀴즈 : 파일의 단어전체수와 3개의 단어만 출력하기 
******************************
파일명 :  data/Yesterday.txt
단어 갯수 :  134
단어 3개 출력
['Yesterday', 'All', 'my']
******************************
파일명 :  data/color.txt
단어 갯수 :  566
단어 3개 출력
['GREEN을', '좋아하는', '사람']
'''

# 퀴즈
# data_eng.txt, data_kor.txt
# 파일안의 데이타의 합과 평균을 구하는
# 함수를 정의하고 아래와 같이 출력하여라
# 함수 정의 => 파일읽기 => 리스트화
# => 리스트의 값 더하기(숫자형데이터로 변환) : 합
# => 합 / 리스트갯수 : 평균

# '''
# # 함수 호출
# sumAvr('data/data_eng.txt', 'cp949')
# sumAvr('data/data_kor.txt', 'cp949')
#
# >> 결과
#
# 파일명 =  data/data_eng.txt
# 데이터 수 =  12
# 합 =  933
# 평균 = 77.75
#
# ----------
# 파일명 =  data/data_kor.txt
# 데이터 수 =  12
# 합 =  892
# 평균 = 74.33
#
# '''
def sumAvr(fileUrl, op):
    f = open(fileUrl,'r', encoding=op)
    dataList = f.readlines() #리스트화
    total = 0
    # 합계 구하기
    for i in dataList:
        score = int(i) # 데이터형 변경
        total += score
    # 평균 구하기
    avr = total/len(dataList)
    print('\n\n','-'*10)
    print('파일명 = ', fileUrl)
    print('데이터 수 = ', len(dataList))
    print('합 = ', total)
    print('평균 = %.2f'%(avr))
    f.close()
sumAvr('data/data_eng.txt', 'cp949')
sumAvr('data/data_kor.txt', 'cp949')


