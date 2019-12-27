# while
cnt = 1
while cnt <= 10:
    print(cnt)
    cnt += 1
print('end')

cnt2 = 1
while cnt2 <= 5:
    print('*' * cnt2)
    cnt2 += 1

# 1~50까지 짝수만 출력하기
cnt3 = 1
while cnt3 <= 50:
    if cnt3 % 2 == 0:
        print(cnt3, end=' ')
    cnt3 += 1
print()
# quiz1 - 3단 출력하기
'''
3 x 1 = 3
3 x 2 = 6
...
3 x 9 = 27
'''
print('-' * 40)
a = 1
while a <= 9:
    print('3 x %d = %d' % (a, 3 * a))
    a += 1

# quiz2 - 1~100까지의 합 출력하기
print('-' * 40)
sum = 0
a = 1
while a <= 100:
    sum += a
    a += 1
print(sum)

# 다중 while문
num1 = 0
while num1 < 5:
    print('-' * 30)
    num2 = 0
    while num2 < 3:
        print('Hello Python')
        num2 += 1
    num1 += 1
