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
