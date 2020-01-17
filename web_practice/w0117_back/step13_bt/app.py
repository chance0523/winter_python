# step13
# use bootstrap
# http://getbootstrap.com/
# 반응형 웹 디자인 (Responsible Web Design)
# 디바이스 (PC/Mobile/Pad)에 따라서 디자인 변경
# local 방식

from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('start2.html')

app.run(host='127.0.0.1',port=5000,debug=True)


