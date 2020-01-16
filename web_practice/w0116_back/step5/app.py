# step5 : html 폼문서(getpost.html) => 서버(python)
# 제어문에 따라서 페이지 분기
from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('getpost.html')

@app.route('/result', methods=['GET','POST'])
def result():
    print(request.method)
    if request.method == 'GET':
        return render_template('get.html')
    else:
        return render_template('post.html')
    


app.run(host='127.0.0.1',port=5000,debug=True)


