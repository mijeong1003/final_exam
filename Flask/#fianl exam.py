#fianl exam
import random
from flask import Flask, request
from flask import render_template
import time
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/RandomNum")                      
def randomnum():
    try:
        global sum
        x=random(1,5000)
        sum+=x
        
        return "ok"
    except:
        return "fail"

sum=0

if __name__ == "__main__":
    app.run(host="0.0.0.0")