# step5
# if문 이용하기

from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)

@app.route('/')
def if1():
    myNum=100
    myNum2=101

    # quiz
    userAge = 26
    return render_template('if1.html', myNum=myNum, myNum2=myNum2, userAge=userAge)



app.run(host='127.0.0.1',port=5000,debug=True)


