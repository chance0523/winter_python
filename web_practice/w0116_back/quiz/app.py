# quiz
# 계산기
# 시작페이지 : calForm.html
# (5) x (6) [버튼]
# 결과
# 5 x 6 = ?
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


