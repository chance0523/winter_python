# step3 : 주소랑 함수랑 html 페이지 연결하기
# render_template 모듈 연결
from flask import Flask
from flask import render_template

app=Flask(__name__)

# render_template('html 문서 경로')
# html 문서는 python 문서를 기준으로 templates 폴더에 있어야한다.
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/one')
def one():
    return render_template('one.html')

@app.route('/two')
def two():
    return render_template('two.html')
    
@app.route('/three')
def three():
    return render_template('three.html')

app.run(host='127.0.0.1',port=5000,debug=True)


