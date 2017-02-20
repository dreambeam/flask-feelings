#!/usr/bin/env python
from flask import Flask

app=Flask(__name__)
#app.debug=True

@app.route('/')
def index():
	return "Hello Bleza"


#if __name__="__main__"

app.run(debug=True, port=8000, host='0.0.0.0')