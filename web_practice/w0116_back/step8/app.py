# step8 : html 폼문서(getForm.html) => 서버(python)
# post 방식으로 전달한 데이터값 출력하기
# html 문서로 전달하기
from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)

@app.route('/')
def postForm():
    return render_template('postForm.html')

@app.route('/resultPost', methods=['POST'])
def resultPost():
    print(request.method)
    # post 방식은 request.form으로 받음.
    data1=request.form['data1']
    data2=request.form['data2']
    data3=request.form['data3']
    data4=request.form['data4']
    print(data1, data2, data3, data4)
    # return render_template('페이지 주소 경로', 변수1=변수11, 변수2=변수22)
    return render_template('postResult.html',data1=data1,data2=data2,data3=data3,data4=data4)

app.run(host='127.0.0.1',port=5000,debug=True)


