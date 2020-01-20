# step1
# 

from flask import Flask
from flask import request
from flask import render_template
import db

app = Flask(__name__)


@app.route('/')
def index():
    user_list=db.get_user_list()
    return render_template('db_user.html', user_list=user_list)


app.run(host='127.0.0.1', port=5000, debug=True)
