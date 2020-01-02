# 파일 쓰기
# 새로운 파일이 생성되면서 내용이 추가된다.
# 기존에 파일이 있다면 덮어쓰기된다.
# 파일변수 = open( 생성파일경로, 'w')
# 파일변수.write(문자열)
# 파일변수.close()

# 빈파일 만들기
f = open('data/test1.txt', 'w')
print('파일이 생성되었습니다.')
f.close()

# 파일 생성후 내용 추가하기
f = open('data/test1.txt', 'w')
print('파일이 생성되었습니다.')
f.write('-' * 10)
f.write('\n테스트 중입니다.\n')
f.write('-' * 10)
# 10 줄 추가하기
for i in range(1, 11):
    f.write('\n%d번째 줄입니다.' % i)
f.close()

# 리스트요소를 정의한 후
# 리스트요소를 파일에 행단위로 저장한다.
myFoodList = ['라면', '김치전', '모밀', '초밥', '샐러드']
line = open('data/myFoodList.txt', 'w')
line.write('\n음식메뉴\n')
for i in myFoodList:
    print(i)
    data = i + '\n'
    line.write(data)
    print('내용이 추가되었습니다.')
line.close()

# 파일을 읽은후 결과값 출력하기
# Yesterday.txt 파일에서 5줄만 추출해서
# resultYesterday.txt 파일에 저장하기
# 파일변수1 = open(읽을파일경로, 'r')
# 리스트변수 = f.readlines()
# 파일변수2 = open(저장할파일경로, 'w')
# for i in ?:
#   파일변수2.write(i)
# 파일변수1.close()
# 파일변수2.close()

# 내용추가하기
# 기존 파일에 내용이 추가된다.
# 파일변수 = open( 생성파일경로, 'a')
# 파일변수.write(문자열)
# 파일변수.close()


# with 문과 파일 입출력
# 파일.close() 를 사용할 필요가 없다.
# with open(파일경로, 'a'/'w'/'r') as 파일변수:
#   명령문
