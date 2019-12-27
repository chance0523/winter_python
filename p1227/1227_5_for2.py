# 자료형의 각 요소 값을 순차적으로 출력
# for 인덱스변수 in 리스트, 문자열, 튜플
# 명령문

# 리스트를 생성하고 아이템을 출력하여라
myList = [2, 3, 5, 7, 11]
for i in myList:
    print(i, end=' ')
print()

myText = '가나다라마바사'
for i in myText:
    print(i, end=' ')
print()

# quiz : 다음 리스트에서 평균, 합, 최댓값, 최솟값, 출력하기
numList = [95, 77, 56, 100, 85]
avg = 0
sum = 0
max = min = numList[0]
for i in numList:
    sum += i
    if max < i:
        max = i
    if min > i:
        min = i
avg = sum / len(numList)
print(f'average = %.2f, sum = %d, max = %d, min = %d' % (avg, sum, max, min))

# for를 이용한 딕셔너리 요소 출력
myDict = {1: '일', 100: '백', 50: '오십', 1000: '천'}
for key in myDict:
    print(key, ':', myDict[key])

# for문과 다중 리스트
listMulti1 = [[1, 2],
              ['a', 'b'],
              ['홍길동', '춘향이']]
print(listMulti1[0])
print(listMulti1[0][0])
print(listMulti1[1][1])
print('--------')
for (i, j) in listMulti1:
    # print('i=',i)
    # print('j=',j)
    print('(i,j)=', i, j)
print('--------')

listMulti2 = [[1, 2, 3],
              ['a', 'b', 'c'],
              ['홍길동', '춘향이', '이몽룡']]
for (i, j, k) in listMulti2:
    print(i, j, k)
