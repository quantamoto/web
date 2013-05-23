import os
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello():
    return render_template('index.html')

