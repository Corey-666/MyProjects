#! /usr/bin/python3.4
# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
def Hello():
    return 'FUCK YOU!!'

if __name__ == '__main__':
    app.run(host='localhost')

