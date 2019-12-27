# range(start, end, step)
# start ~ (end-1)까지 step만큼 차례대로 숫자 생성. ☆ range 객체로 생성.
print('---range---')
print(range(1, 11))
print(list(range(1, 11)))
print(tuple(range(1, 31, 2)))
print(set(range(0, 31, 2)))

# for 인덱스변수 in range(start, end, step)
# 1~10까지 출력하기
for i in range(1, 11):
    print(i, end=' ')
print()

# 1~10까지 홀수만 출력하기
for i in range(1, 11, 2):
    print(i, end=' ')
print()

# 1~100 사이의 합 구하기
sum = 0
for i in range(1, 101):
    sum += i
print('1~100까지의 합 :', sum)

# for문에서 조건문 실행
# 한줄에 1~25까지 5개씩 출력하기
'''
1 2 3 4 5
6 7 8 9 10
...
21 22 23 24 25
'''
for i in range(1, 26):
    if i % 5 == 0:
        print(i)
    else:
        print(i, end=' ')

# 1~25에서 5의 배수만 빼고 출력
for i in range(1, 25):
    if i % 5 == 0:
        continue
    else:
        print(i, end=' ')
print()

# 다중 for문
for i in range(0, 3):
    print('-' * 30)
    for j in range(0, 3):
        print('Hello World')

# 다중 for문 이용 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print('%d x %d = %d' % (i, j, (i * j)))
    print('%d단 끝' % i)

# list for
# 1~10가지 숫자로 이루어진 리스트 만들기 1
numList = []
for i in range(1, 11):
    numList.append(i)
print(numList)

# 1~10가지 숫자로 이루어진 리스트 만들기 1
numList = [i for i in range(1, 11)]
print(numList)

# 3의 배수에서 -1 한 값으로 리스트를 만들어라
numList = [(i * 3) - 1 for i in range(1, 10)]
print(numList)

starList=['*'*i for i in range(1,10)]
print(starList)