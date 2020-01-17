# step4
# for문을 이용해서 집합자료 (딕셔너리, 리스트, 튜플)

from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)

@app.route('/')
def forCollection():
    myList=['구로동','신도림동','서초동','잠원동']
    for item in myList:
        print(item)

    myTuple = ('라면','짜장면','짬뽕')
    for item in myTuple:
        print(item)

    myDict = {'one':1,'two':'둘','three':3}
    for key in myDict:
        print(key, ':', myDict[key])

    return render_template('forCollection.html',
    myList=myList, myTuple=myTuple, myDict=myDict)



app.run(host='127.0.0.1',port=5000,debug=True)


