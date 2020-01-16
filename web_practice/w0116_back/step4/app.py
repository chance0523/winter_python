# step4 : html 폼문서(getpost.html) => 서버(python)
# request 연결 : 폼문서를 파이썬과 연결
from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('getpost.html')

@app.route('/result',methods=['GET','POST'])
def result():
    # request.method => html에서 전송방식(method) 표시
    print(request.method)
    return '<h1>연결완료</h1><p><a href="/">첫페이지로 이동</a></p>'


app.run(host='127.0.0.1',port=5000,debug=True)


