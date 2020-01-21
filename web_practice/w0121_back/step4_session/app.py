# step1
#

from flask import Flask, request, session
from flask import render_template
import db

app = Flask(__name__)
# secret key
app.secret_key = 'qwe123!@#'

@app.route('/')
def index():
    return render_template('index_login.html')

@app.route('/login_pro',methods=['GET'])
def login_pro():
    userId = request.args['userId']
    password = request.args['password']
    login_result = db.login_result(userId,password)
    # True => session 안에 userId 저장. 로그인 후 페이지로 연결. logined.html
    # False => 회원 가입 페이지로 연결. memberJoin.html
    if login_result:
        # 세션 저장 : session[변수] = 값
        session['userId']=userId
        return render_template('logined.html',userId=userId)
    else:
        return render_template('memberJoin.html')

@app.route('/logout')
def logout():
    # 세션 아웃 1 : del session[변수]
    # 세션 아웃 2 : session.pop(변수, None)
    del session['userId']
    return render_template('index_login.html')
app.run(host='127.0.0.1', port=5000, debug=True)
