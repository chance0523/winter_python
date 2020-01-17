# step2
# 서버(python) app.py
# 딕셔너리, 리스트, 문자열 데이터 정의
# => html 페이지로 값 출력하기
from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)

@app.route('/')
def dataTrans():
    data1 = 100
    data2 = 'Hello World'
    data3 = ['apple','bannana','grape']
    data4 = ['do','re','me']
    data5 = {'a':'africa','b':'boat','c':'cat'}
    return render_template('dataTransResult.html', data1=data1, data2=data2, data3=data3, data4=data4, data5=data5)



app.run(host='127.0.0.1',port=5000,debug=True)


