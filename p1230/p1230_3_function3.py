# 외장함수 : 별도의 import 명령이 필요하다. 함수(옵션)
# 내장함수 : 별도의 import 명령이 필요없다. 모듈.함수(옵션)

# 시간과 관련된 모듈 임포트
import datetime

# 현재 시간을 기준으로 년, 월, 일, 시, 분, 초 변수 생성
now = datetime.datetime.now()
print(now)
print('연도 :', now.year)
print('월 :', now.month)
print('날짜 :', now.day)
print('시간 :', now.hour)
print('분 :', now.minute)
print('초 :', now.second)

print(f'오늘은 {now.year}년 {now.month}월 {now.day}일 입니다.')
print(f'현재시간은 {now.hour}시 {now.minute}분입니다.')
print(f'현재시간은 {now.hour - 12}시 {now.minute}분입니다.')
