# step1
#

from flask import Flask
from flask import request
from flask import render_template
import db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('start.html')


app.run(host='127.0.0.1', port=5000, debug=True)
