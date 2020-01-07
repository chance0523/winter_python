import csv

# csv 파일 쓰기 (데이터 기준)
# 리스트 안에 리스트 => csv
# 리스트 안에 딕셔너리 => csv
# 1행은 column 제목용도로 사용 -> Header

# 리스트 데이터를 csv 파일 쓰기 1
# 리스트는 2차원이어야 한다.
# [[1행...], [2행...]]

# 파일 변수 = open(csv파일경로, 'w', newline = '공백\/r', encoding = 'utf-8/cp949')
# csv변수 = csv.writer(파일변수)

# for row in 리스트:
#    csv변수.writerow(row)
# 파일변수.close()

# csv 파일에 저장될 2차원 리스트
# 1행은 제목용도
myList = [['이름', '주소', '전화번호'],
          ['김영희', '부산시', '010-6374-9087'],
          ['홍길동', '춘천시', '010-5463-9403'],
          ['성은희', '서울시', '010-4646-9403']]

# 행과 행 사이에 공백 생성 : newline='\r'
# f = open('data/addr1.csv', 'w', encoding='cp949')
# 공백 행 없이 쓰기 : newline=''
f = open('data/addr1.csv', 'w', newline='', encoding='cp949')
csvline = csv.writer(f)
for row in myList:
    csvline.writerow(row)
print('파일쓰기가 완료되었습니다')
f.close()

# with문으로 교체
with open('data/addr11.csv', 'w', newline='', encoding='cp949') as f:
    csvline = csv.writer(f)
    for row in myList:
        csvline.writerow(row)
    print('파일쓰기가 완료되었습니다.')

# 내용 추가
# 파일변수 = open(csv파일경로, 'a', newline='', encoding='utf-8/cp949')
# csv변수 = csv.writer(파일변수)
# for row in 리스트데이터변수:
#   csv변수.writerow(row)
# 파일변수.close()

myList1 = [['이름', '주소', '전화번호'],
           ['이영희', '부산시', '010-6374-9087'],
           ['양수정', '춘천시', '010-5463-9403']]
f = open('data/addr1.csv', 'a', newline='', encoding='cp949')
csvline = csv.writer(f)
# 1행의 제목 헤더행은 제외하고 2행부터 추가
for row in myList1[1:]:
    csvline.writerow(row)
print('내용이 추가되었습니다.')
f.close()

# 'data/population.csv' 파일에서 11개의 데이터행을 추출해서
# 'data/population_11.csv' 파일로 쓰기

# 파일을 읽고 리스트안에 리스트 구조로 만들기
with open('data/population.csv', 'r') as f:
    csv_data = csv.reader(f)
    # for row in csv_data:
    #     print(row)
    # 리스트 안에 리스트 구조로 저장하기
    list_pop =[]
    for row in csv_data:
        list_pop.append(row)
    print(list_pop)
