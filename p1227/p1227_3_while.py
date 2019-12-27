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
