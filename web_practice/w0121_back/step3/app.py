# step1
#

from flask import Flask
from flask import request
from flask import render_template
import db

app = Flask(__name__)


@app.route('/')
def index():
    result_list = db.get_emp_list()
    total_count = db.get_total_count()
    total_page = int(total_count/5)+1
    return render_template('start.html', result_list=result_list, total_count=total_count, total_page=total_page)


@app.route('/page_list', methods=['GET'])
def page_list():
    n = int(request.args['page'])
    m = 5
    result_list = db.get_page_list(n, m)
    total_count = db.get_total_count()
    total_page = int(total_count/5)+1
    return render_template('start.html', result_list=result_list, total_count=total_count, total_page=total_page)


app.run(host='127.0.0.1', port=5000, debug=True)
