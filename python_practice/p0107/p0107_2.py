import csv

# 딕셔너리 안에 딕셔너리 -> csv
# 딕셔너리 리스트 데이터를 csv 파일 쓰기 1
# 파일쓰기 용도의 데이터 구조는
# 딕셔너리 리스트 : 리스트 안에 딕셔너리가 있는 구조
# [{키1:값1, 키2:값2 ... }, ... ,{ ... }]

# csv변수 = csv.Dictwriter(파일변수)
# 제목 용도의 별도의 리스트 생성
# 키리스트변수 = [키1, 키2, ...]
# for row in 리스트데이터변수:
#   csv변수.writerow(row)
# 파일변수.close()

# 딕셔너리 리스트
dict_list1 = [
    {'first-name': 'Pildong', 'last-name': 'Chang'},
    {'first-name': 'Jeongjoon', 'last-name': 'Seo'},
    {'first-name': 'Hajin', 'last-name': 'Bhang'}
]
field_list = ['first-name', 'last-name']

with open('data/names1.csv', 'w', newline='') as f:
    csvline = csv.DictWriter(f, fieldnames=field_list)
    # 제목행 쓰기 : csv변수.writeheader()
    csvline.writeheader()
    for row in dict_list1:
        print(row)
        csvline.writerow(row)

dict_list2 = [
    {'first-name': 'James', 'last-name': 'Dean'},
    {'first-name': 'Tom', 'last-name': 'Cruz'},
]
f = open('data/names1.csv', 'a', newline='')
csvline = csv.DictWriter(f, fieldnames=field_list)
for row in dict_list2:
    csvline.writerow(row)
f.close()

dict_list3 = []

field_list2 = ['State', 'Population']
with open('data/population_22.csv', 'w', newline='') as f:
    csvline = csv.DictWriter(f, fieldnames=field_list2)
    # 제목행 쓰기 : csv변수.writeheader()
    csvline.writeheader()
    for row in dict_list3:
        print(row)
        csvline.writerow(row)

# quiz1. data.csv 파일에서 class 필드명의 값이 1인 학생만 별도 파일에 저장 (data_class1.csv)
# 저장 할 때 class 필드 빼고

with open('data/data.csv', 'r') as f:
    class_list = ['class', 'name', 'kor', 'eng', 'mat', 'bio']
    class1list = []
    csvdata = csv.DictReader(f, fieldnames=class_list)
    for row in csvdata:
        if row['class'] == '1':
            class1list.append(row)
with open('data/data_class1.csv', 'w', newline='') as f:
    class_list.pop(0)
    csvline = csv.DictWriter(f, fieldnames=class_list)
    csvline.writeheader()
    for row in class1list:
        del row['class']
        csvline.writerow(row)

# quiz2. data.csv 파일에서
# (class, name, kor, eng, mat, bio)
# (class, name, kor, eng, mat, bio, total, avg)
# data_class2.csv 에 저장
with open('data/data.csv', 'r') as f:
    field_list = ['class', 'name', 'kor', 'eng', 'mat', 'bio']
    getlist = []
    csvdata = csv.DictReader(f, fieldnames=field_list)
    for row in csvdata:
        getlist.append(row)
    # print(getlist)
    for row in getlist[1:]:
        row['total'] = (int(row['kor']) + int(row['eng']) + int(row['mat']) + int(row['bio']))
        row['avg'] = (int(row['kor']) + int(row['eng']) + int(row['mat']) + int(row['bio'])) / 4

with open('data/data_class2.csv', 'w', newline='') as f:
    field_list2 = ['class', 'name', 'kor', 'eng', 'mat', 'bio', 'total', 'avg']
    csvline = csv.DictWriter(f, fieldnames=field_list2)
    csvline.writeheader()
    for row in getlist[1:]:
        csvline.writerow(row)
