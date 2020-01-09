# CSV
# data 폴더에서 csv 파일 확인
# population.sv / data.csv / koreaTraffic.csv
# data.go.kr 에 들어가면 공공 data들이 있음

# CSV란?
# Comma Seperate Value
# Comma( , ) 로 데이터가 분류

# 내장 모듈 import
import csv

# CSV file 읽기
# 파일변수 = open('csv파일경로', 'r', encoding = 'utf-8/cp949')
f = open('data/data.csv', 'r', encoding='utf-8')
csv_data = csv.reader(f)
print(type(csv_data))
# for line in csv_data:
#     print(line,type(line))

# 리스트 안에 리스트 구조로 변경
data_list = []
for i in csv_data:
    data_list.append(i)

print(data_list, '행의 갯수', len(data_list))
for i in data_list:
    print(i, '열의 갯수', len(i))

# 첫번째 행은 제목
print(data_list[0])
# 1행 1열 출력
print(data_list[0][0])
# 마지막 행의 마지막 열
print(data_list[-1][-1], type(data_list[-1][-1]))  # 문자열

# kor 데이터만 정수형으로 (1행은 str('kor')이라 제외)
korList = []
# korList.append(data_list[0][2])
for i in range(1, len(data_list)):
    korList.append(int(data_list[i][2]))
print(korList)

# kor 과목의 총합과 평균을 구해라
print(f'kor 과목의 총점 : {sum(korList)}')
print(f'kor 과목의 평균 : {sum(korList) / len(korList)}')
print(f'kor 과목의 최고점 : {max(korList)}')
print(f'kor 과목의 최저점 : {min(korList)}')

# quiz
# 4과목의 총점, 평균
korList = []
engList = []
matList = []
bioList = []
for i in range(1, len(data_list)):
    korList.append(int(data_list[i][2]))
    engList.append(int(data_list[i][3]))
    matList.append(int(data_list[i][4]))
    bioList.append(int(data_list[i][5]))
print('kor =', korList)
print('eng =', engList)
print('mat =', matList)
print('bio =', bioList)
print(f'4과목의 총점 합 : {(sum(korList + engList + matList + bioList))}')
print(f'4과목의 평균 : {(sum(korList + engList + matList + bioList)) / len(korList + engList + matList + bioList)}')

f.close()

# 국어 점수의 최고점을 받은 학생의 이름은?
# 국어점수의 최고점을 구한다. max()
# 최고점의 인덱스를 구한다. 리스트이름.indexof()
# 인덱스를 학생이름 인덱스에 삽입한다.

print(f'kor 과목의 최고점 : {max(korList)}')
print(f'최고점의 index는? {korList.index(max(korList))}')
print(f'kor 과목의 최고점을 받은 학생의 이름 : {data_list[korList.index(max(korList))][1]}')