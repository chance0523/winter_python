# step9
# 이미지 삽입하기
# 이미지경로는 ? app.py를 기준으로 static 폴더에 있어야한다.

from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('imageGallery.html')


app.run(host='127.0.0.1',port=5000,debug=True)


