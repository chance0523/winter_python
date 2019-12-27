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

# while문을 이용한 (리스트, 딕셔너리, 문단, 집합, 튜플 아이템 출력)
i = 0
list1 = ['사과', '바나나', '수박', '포도']
while i < len(list1):
    print(i, '번째 요소는', list1[i])
    i += 1
print('-' * 30, '\n\n')

# 짝수번째 글자만 출력하기
i = 0
txt1 = '가나다라마바사'
while i < len(txt1):
    print(i, '번째 요소는', txt1[i])
    i += 2

# 딕셔너리 구조에서 키와 값을 분리시켜서 출력하기

