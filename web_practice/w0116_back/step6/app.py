# step6 : html 폼문서(getForm.html) => 서버(python)
# get 방식으로 전달한 데이터값 출력하기
from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)

@app.route('/')
def getForm():
    return render_template('getForm.html')

@app.route('/resultGet', methods=['GET'])
def resultGet():
    print(request.method)
    # get으로 전달되는 데이터값
    # request.args[변수명(=name)]
    data1=request.args['data1']
    data2=request.args['data2']
    print(data1, data2)
    return f'data1={data1}, data2={data2} <p><a href="/">첫페이지로 이동</a></p>'

app.run(host='127.0.0.1',port=5000,debug=True)


