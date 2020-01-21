# step1
# 

from flask import Flask
from flask import request
from flask import render_template
import db

app = Flask(__name__)


@app.route('/')
def index():
    country_list=db.get_country_list()
    return render_template('start.html', country_list=country_list)

# 레코드 추가 페이지 주소
@app.route('/add_record')
def add_record():
 return render_template('add_record.html')

# 레코드 전송 완료 페이지 주소
@app.route('/add_record_pro', methods=['post'])
def add_record_pro():
 # post 입력 데이타를 변수에 저장한다.
 # 변수명 = request.form[폼요소의name값]
 c_code = request.form['c_code']
 c_name = request.form['c_name']
 c_continent = request.form['c_continent']
 c_population = request.form['c_population']
 c_gnp = request.form['c_gnp']
 print(c_population)
 # 레코드 추가 함수 호출
 db.add_record(c_code, c_name, c_continent, c_population, c_gnp)
 # 레코드 목록 호출
 country_list = db.get_country_list()
 return render_template('start.html', country_list=country_list)

@app.route('/delete_record')
def delete_record():
    country_list=db.get_country_list()
    return render_template('delete_record.html', country_list=country_list)

# 레코드 삭제 실행 페이지 주소
@app.route('/delete_record_pro', methods=['GET'])
def delete_record_pro():
    # 하이퍼링크의 데이터값 전달받기
    c_code = request.args['c_code']
    # 삭제함수 호출
    db.delete_record(c_code)
    country_list=db.get_country_list()
    return render_template('start.html',country_list=country_list)

# 레코드 상세 페이지 주소
@app.route('/view_record',methods=['GET'])
def view_record():
 # 하이퍼링크의 데이타값 전달받기
 c_code = request.args['c_code']
 print(c_code)
 # 특정 레코드 출력 함수

 # # 레코드 목록 호출
 country_list = db.view_record(c_code)
 return render_template('view_record.html', country_list=country_list )

# update_record
@app.route('/update_record',methods=['GET'])
def update_record():
 # 하이퍼링크의 데이타값 전달받기
 c_code = request.args['c_code']
 c_name = request.args['c_name']
 c_continent = request.args['c_continent']
 c_population = request.args['c_population']
 c_gnp = request.args['c_gnp']
 # return c_name, c_gnp
 return render_template('update_record_form.html', c_code=c_code, c_name=c_name,c_continent=c_continent, c_population=c_population, c_gnp=c_gnp )


@app.route('/update_record_pro', methods=['post'])
def update_record_pro():
 c_code = request.form['c_code']
 c_name = request.form['c_name']
 c_continent = request.form['c_continent']
 c_population = request.form['c_population']
 c_gnp = request.form['c_gnp']
 # 레코드 수정 함수 호출
 db.update_record(c_name, c_continent, c_population, c_gnp, c_code)

 # 레코드 목록 호출
 # country_list = db.get_country_list()
 # return render_template('start3.html', country_list=country_list)

 # # 레코드 목록 호출
 country_list = db.view_record(c_code)
 return render_template('view_record.html', country_list=country_list)


app.run(host='127.0.0.1', port=5000, debug=True)
