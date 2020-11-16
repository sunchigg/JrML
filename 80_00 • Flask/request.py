# -*- coding: utf-8 -*-
"""可於local端輸入以下：
http://127.0.0.1:5000/index?name=test&age=666
Output:hello Flask. ur name=test and age=666
"""
from flask import Flask, request

app = Flask(__name__)


@app.route("/index", methods=["GET", "POST"])
def index():
    name = request.args.get("name")
    age = request.args.get("age")
    return "hello Flask. ur name=%s and age=%s" % (name, age)


if __name__ == '__main__':
    app.run(debug=True)
