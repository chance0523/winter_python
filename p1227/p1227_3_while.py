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
dict1 = {'a': 'africa', 's': 'say', 'c': 'coffee', 'd': 'drama', 'y': 'yes'}
key2list = list(dict1.keys())
val2list = list(dict1.values())
i = 0
while i < len(key2list):
    print(key2list[i], ':', val2list[i])
    i += 1

# 리스트에서 가장 큰 값 구하기
myNumList = [100, 200, 50, -30, 999, 10]
print('Before = ', myNumList)
cnt = 0
max = myNumList[0]
while cnt < len(myNumList):
    if max < myNumList[cnt]:
        max = myNumList[cnt]
    cnt += 1
print('max =', max)

# 리스트에서 요소 삭제
# 리스트변수.pop() : 마지막 삭제
# 리스트변수.pop(index) : index value 삭제
# 리스트변수.remove(value) : 해당 value 삭제
myNumList.remove(max)
print('myNumList =', myNumList)

print('-' * 30, '\n\n')
# quiz1
# 가장 큰 수와 가장 작은 수를 삭제
print('---quiz1---')
myNumList = [100, 200, 50, -30, 999, 10, -30]
min = max = myNumList[0]
myNumList = list(set(myNumList))
cnt = 0
print(f'myNumList = {myNumList}')
while cnt < len(myNumList):
    if max < myNumList[cnt]:
        max = myNumList[cnt]
    if min > myNumList[cnt]:
        min = myNumList[cnt]
    cnt += 1
myNumList.remove(max)
myNumList.remove(min)
print('최솟값과 최댓값을 삭제한 뒤의 myNumList =', myNumList)

# quiz2
# 딕셔너리 값이 'a' 글자가 있는 아이템만 표시하고 총 갯수 출력하기
print('---quiz2---')
'''
'a' : 'africa
's' : 'say'
'd' : 'drama'
총 갯수는 ? 3
'''
dict2 = {'a': 'africa', 's': 'say', 'c': 'coffee', 'd': 'drama', 'y': 'yes'}
key2list = list(dict2.keys())
val2list = list(dict2.values())
i = 0
cnt = 0
while i < len(val2list):
    if 'a' in val2list[i]:
        print(f'{key2list[i]} : {val2list[i]}')
        cnt += 1
    i += 1
print('총 갯수는?', cnt)

# quiz3
# 다음 문자열을 사선으로 한 글짜씩 출력하여라
print('---quiz3---')
message = 'Hello Python'
gongback = 0
while gongback < len(message):
    print(' ' * gongback + message[gongback])
    gongback += 1

# break
count = 0
while count < 2:
    print('Hello Python')
    count += 1
    break
print('Hello Python2')

print('-' * 30)
count = 0
while count < 2:
    print('Hello Python')
    count += 1
    continue
print('Hello Python2')
