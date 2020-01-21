# step1
#

from flask import Flask, request, session, redirect
from flask import render_template
import db

app = Flask(__name__)
# secret key
app.secret_key = 'qwe123!@#'


@app.route('/')
def index():
    return render_template('index_login.html')


@app.route('/login_pro', methods=['GET'])
def login_pro():
    userId = request.args['userId']
    password = request.args['password']
    login_result = db.login_result(userId, password)
    user_data = db.view(userId)
    # True => session 안에 userId 저장. 로그인 후 페이지로 연결. logined.html
    # False => 회원 가입 페이지로 연결. memberJoin.html
    if login_result:
        # 세션 저장 : session[변수] = 값
        session['userId'] = userId
        return render_template('logined.html', userId=userId)
    else:
        return render_template('memberJoin.html')

@app.route('/join')
def join():
    return render_template('memberJoin.html')

@app.route('/join_pro', methods=['POST'])
def join_pro():
    # post 입력 데이터를 변수에 저장한다.
    # 변수명 = request.form[폼요소의name값]
    userId = request.form['userId']
    password = request.form['password']
    email = request.form['email']

    db.join(userId, password, email)

    return render_template('join_complete.html')


@app.route('/logout')
def logout():
    # 세션 아웃 1 : del session[변수]
    # 세션 아웃 2 : session.pop(변수, None)
    del session['userId']
    return redirect('/')

# render_template(주소, 전달변수=전달변수값)
# redirect(주소)

@app.route('/view',methods=['GET'])
def view():
    userId = request.args['userId']

    result_data = db.view(userId)
    return render_template('view.html', result_data=result_data)

@app.route('/update',methods=['GET'])
def update_record():
    userId = request.args['userId']
    password = request.args['password']
    email = request.args['email']
    return render_template('update.html', userId=userId, password=password, email=email)


@app.route('/update_pro', methods=['POST'])
def update_record_pro():
    userId = request.form['userId']
    password = request.form['password']
    email = request.form['email']

    db.update_record(password, email, userId)

    result_data = db.view(userId)
    return render_template('view.html', result_data=result_data)


app.run(host='127.0.0.1', port=5000, debug=True)
