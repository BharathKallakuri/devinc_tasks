from flask import Flask
from requests import *
import json

app = Flask(__name__)

@app.route("/calculator",methods=["POST"])
def calculator():
    if request.method == "POST":
        a = int(request.form["first"])
        b = int(request.form["second"])
        operator = request.form["operator"]
        if operator == "add":
            ans = a + b
        elif operator == "sub":
            ans = a - b
        elif operator == "mul":
            ans = a*b
        elif operator == "div":
            ans = a/b
        else:
            ans = "Invalid operation"

        return json.dumps({"result" : ans})