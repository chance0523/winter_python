# step2 : 주소랑 연결하기
from flask import Flask

app=Flask(__name__)

@app.route('/')
def home(): # root는 보통 home으로
    return '<h1>Home</h1><p><a href="/test">test로 이동</a></p>'

@app.route('/test')
def test():
    return '<h1>Test</h1><p><a href="/">home으로 이동</a></p>'

app.run(host='127.0.0.1',port=5000,debug=True)


