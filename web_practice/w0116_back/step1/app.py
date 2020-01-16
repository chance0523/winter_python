from flask import Flask

# app 생성
app=Flask(__name__)

# 라우터 생성
# 라우터란? 주소생성 => 함수와 연결
'''
@app.route(경로)
def 함수:
    명령문
    return 결과값(데이터 또는 html태그)
'''

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/test')
def test():
    return 'test'
    
# 앱 실행
app.run(host='127.0.0.1',port=5000,debug=True)


