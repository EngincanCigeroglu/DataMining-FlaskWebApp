from datetime import datetime
import json
from pathlib import Path
import pickle
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import numpy as np

app = Flask(__name__)

@app.route("/")
@app.route("/register.html")
def home():
    return render_template('register.html')


@app.route('/result_recommend.html',methods = ['POST'])
def result_recommend():
    if request.method == 'POST':
         return render_template('result_recommend.html')


if __name__ == "__main__":
    app.run()


