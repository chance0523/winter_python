# step2
# 반복문 사용

from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)

@app.route('/')
def forRange():
    for i in range(1,11):
        print(i)
    return render_template('forRange.html')



app.run(host='127.0.0.1',port=5000,debug=True)


