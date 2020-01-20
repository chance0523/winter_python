# step2
# 딕셔너리 구조로 테이블 데이터 불러온 후 테이블 구조로 출력

from flask import Flask
from flask import request
from flask import render_template
import db

app = Flask(__name__)


@app.route('/')
def index():
    country_list=db.get_country_list()
    return render_template('db_table.html', country_list=country_list)


app.run(host='127.0.0.1', port=5000, debug=True)
