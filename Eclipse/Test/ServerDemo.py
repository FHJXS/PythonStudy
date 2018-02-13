# -*- coding: utf-8 -*-
'''
Created on 2018年2月12日

@author: www60
'''
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "hellowolrd"


if __name__ == '__main__':
    app.run()
