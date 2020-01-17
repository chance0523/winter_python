# step3
# 반복문 사용
# 구구단 출력
from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)

@app.route('/')
def forRange2():
    for i in range(2,10):
        for j in range(1,10):
            print(i,'x',j,'=',i*j)
    return render_template('forRange2.html')



app.run(host='127.0.0.1',port=5000,debug=True)


