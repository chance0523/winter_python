import csv

# with문 이용 CSV 파일 열기
with open('data/population.csv', 'r', encoding='cp949') as f:
    csv_data = csv.reader(f)
    print(csv_data, type(csv_data))

    # for row in csv_data:
    #     print(row)

    # 리스트 구조로 변경하기
    resultList = []
    for i in csv_data:
        resultList.append(i)
    print(resultList)
    print(len(resultList))  # 행 수 52
    print(len(resultList[0]))  # 열 수 2

    # 1행은 컬럼 제목이므로 삭제
    resultList.pop(0)
    print(resultList)

    # stateList 를 정렬
    stateList = []
    for i in resultList:
        stateList.append(i[0])
    print(stateList)
    # stateList.sort()
    # print(stateList)
    # stateList.reverse()
    # print(stateList)

    # quiz
    # 인구수의 최대는?
    # 주의할점 : 4700000이 아니라 4,700,000으로 되어있음
    # , 를 삭제하고 int(). replace(',','')
    popList = []
    for i in resultList:
        popList.append(int(i[1].replace(',', '')))
    print(popList)
    print(max(popList))
    print(stateList[popList.index(max(popList))])

    popList2 = []
    for i in resultList:
        popList2.append(i[1])
        # print(i)
    print(', 제거 전:', popList2)
    # for i in popList2:
    #     temp = i.replace(',', '')
    #     print(i, temp)
    for i in range(0, len(popList2)):
        popList2[i] = popList2[i].replace(',', '')
    print(', 제거 후:', popList2)

print('\n\n')

with open('data/koreaTraffic.csv', 'r') as f:
    # csv_data = csv.reader(f)
    csv_data = csv.DictReader(f)
    print(csv_data, type(csv_data))

    # for row in csv_data:
    #     print(row, type(row))

    # for row in csv_data:
    #     print(row['구분'], row['일반인'], type(row['구분']))

    # 가장 작은 일반인 사용자의 수는?
    list1 = []
    for row in csv_data:
        list1.append(int(row['일반인']))
    print(min(list1))
    # 일반인 사용자가 가장 적은 도시는?
    print(list1.index(min(list1)))

# 일반인+청소년+어린이 합해서 지역별 사용자 구하기
with open('data/koreaTraffic.csv', 'r') as f:
    csv_data = csv.DictReader(f)
    list_city = []
    list_user = []
    for row in csv_data:
        list_city.append(row['구분'])
        list_user.append(int(row['일반인']) + int(row['청소년']) + int(row['어린이']))
    print(list_city)
    print(list_user)

    # 제주 사용자의 총 데이터 값 출력
    print('제주 인덱스 =>', list_city.index('제주'))
    print('제주의 사용자수 =>', list_user[list_city.index('제주')])

    # 딕셔너리 구조로 변경하기
    # {도시명 : 인구 사용자 총수, ... }
    korea_traffic_dict = {}
    for i in range(0, len(list_city)):
        korea_traffic_dict[list_city[i]] = list_user[i]
    print(korea_traffic_dict)

    print(korea_traffic_dict['강원'])

    # quiz1. 시도대학별기업규모에따른취업자수.csv
    # 파일 읽기
    # quiz2. 1000명 이상인 회사에 들어간 취업자수가 가장 많은 도시는?
    # quiz3.
    # 딕셔너리로 (DictReader) 만들기
    # {'지역명' : '분석대상자수' ... }
