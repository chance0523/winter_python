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
    print(popList2)
    for i in popList2:
        i.replace(',', '')
    print(popList2)
