from flask import Flask, render_template, session, redirect, url_for

# ==================================================
# インスタンス生成
# ==================================================
app = Flask(__name__)
import os
# 乱数を設定
app.config['SECRET_KEY'] = os.urandom(24)

# ==================================================
# ルーティング
# ==================================================
from forms import InputForm

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/input_home')
def input_home():
    return render_template('input_home.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/input_calendar')
def input_calendar():
    return render_template('input_calendar.html')

@app.route('/folder')
def folder():
    return render_template('folder.html')

if __name__ == '__main__':
    app.run()