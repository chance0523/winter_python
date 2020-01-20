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

@app.route('/record_view',methods=['GET'])
def record_view():
    c_code=request.args['c_code']
    c_name=request.args['c_name']
    c_continent=request.args['c_continent']
    c_population=request.args['c_population']
    c_gnp=request.args['c_gnp']

    country_list=[c_code,c_name,c_continent,c_population,c_gnp]

    return render_template('record_view.html',country_list=country_list)

app.run(host='127.0.0.1', port=5000, debug=True)
