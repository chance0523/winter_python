# 사용자 정의 모듈

# 같은 폴더에 저장
# # test.py
# def testPrint():
#     print("모듈 테스트")

# 사용자 정의 모듈 임포트
# import 사용자정의파일명
import test
# 사용자정의모듈안에 있는 함수 호출
test.testPrint()
test.sum(10,20)

# 퀴즈1 - 구구단 모듈
# Step1. gugu.py로 입력한 숫자에 대한 구구단을 출력하는 모듈파일 생성
# Step2. import gugu로 모듈을 임포트 한 후 모듈이 실행되는지 확인

# 퀴즈2 - 로또 모듈
# Step1.lotto.py로 갯수 지정시 자동으로 생성되는
#       로또 번호를 리턴하는 모듈파일 생성
# Step2. import lotto로 모듈을 임포트 한 후
#       모듈이 실행되는지 확인

# from gugu import guguPrint
# import gugu as g
import gugu
gugu.guguPrint(5)

import lotto
lotto.lottoNum(5)
lotto.lottoNum(10)

# --------------
# 패키지(Package)
# 모듈파일을 별도의 폴더에 저장하여 쓰는 기능
# 폴더는 패키지명으로 이용

# 패키지 생성후 함수 호출은?
# 1
# import 패키지명.모듈명
# 패키명.모듈명.함수(인자)
# 2
# import 패키지명.모듈명 as 별칭
# 별칭.함수(인자)
# 3
# from 패키지명.모듈명 import 함수
# 함수(인자)

# 파이참에서 패키지용도의 폴더만들기
# [Project] 창에서 폴더 마우스우측버튼
# [New]-[python package]
# 패키지폴더가 생성되고 자동으로 __init__.py 파일 생성
# __init__.py
# : 패키지폴더임을 알려주는 파일

# 별도패키지폴더명 - AAA
# 패키지안의 모듈 파일 - AAA/a.py
# 모듈파일안에 함수 정의 - testPrint()

# import AAA.a
# AAA.a.testPrint()

# import AAA.a as A
# A.testPrint()

from AAA.a import testPrint
testPrint() # AAA패키지안의 a.py


# 별도패키지폴더명 - AAA/BBB
# 패키지안의 모듈 파일 - AAA/BBB/b.py
# 모듈파일안에 함수 정의 - testPrintB()
# import AAA.BBB.b
# AAA.BBB.b.testPrintB()

# import AAA.BBB.b as B
# B.testPrintB()

from AAA.BBB.b import testPrintB
testPrintB() # AAA/BBB 패키지안의 b.py


# 별도패키지폴더명 - CCC
# CCC 패키지안에서 모듈 파일 생성
# CCC/c1.py => testC1() 함수 정의
# CCC/c2.py => testC2() 함수 정의

# import CCC.c1, CCC.c2
# CCC.c1.testC1()
# CCC.c2.testC2()

# 패키지로 정의된 폴더안의 __init__.py
# __all__ = [모듈명1, 모듈명2...]
# CCC/__init__.py
# __all__ = ['c1', 'c2']

# from 패키지명 import *
# 함수 호출
# 모듈명.함수명으로 호출가능

from CCC import *
c1.testC1()
c2.testC2()


