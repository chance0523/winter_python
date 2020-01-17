# step6
# query string : 주소에 값을 전달하기
# app.py => 첫 페이지 : 하이퍼링크에 값을 전달하기
# app.py의 처리 라우터 => 결과 html

from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('queryString1.html')

# @app.route('/라우터주소/<데이터변수>')
@app.route('/resultQuery/<num>')
def resultQuery(num):
    return render_template('gugu_result.html',num=int(num))

app.run(host='127.0.0.1',port=5000,debug=True)


