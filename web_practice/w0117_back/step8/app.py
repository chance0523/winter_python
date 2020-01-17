# step8.quiz
# query string : 값을 전달해서 1부터 값까지의 합을 구해서 결과 출력
# app.py => 첫 페이지 : 하이퍼링크에 값을 전달하기
# app.py의 처리 라우터 => 결과 html

from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('queryString2.html')

# @app.route('/라우터주소/<데이터변수>')
@app.route('/resultQuery2/<num>')
def resultQuery(num):
    sum=0
    num=int(num)
    for i in range(1,num+1):
        sum+=i
    return render_template('sum2n.html',num=num,sum=sum)

app.run(host='127.0.0.1',port=5000,debug=True)


