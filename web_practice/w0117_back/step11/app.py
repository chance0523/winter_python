# step11
# 상속이란? = 인클루드
# 웹사이트에서 반복적인 부분(메뉴, 카피라이트)을
# 별도의 공통 부분으로 등록
# 상속명령을 이용해서 삽입하는 기능

from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('menu1.html')

@app.route('/menu2')
def menu2():
    return render_template('menu2.html')

@app.route('/menu3')
def menu3():
    return render_template('menu3.html')

@app.route('/menu4')
def menu4():
    return render_template('menu4.html')

@app.route('/menu5')
def menu5():
    return render_template('menu5.html')

app.run(host='127.0.0.1',port=5000,debug=True)


