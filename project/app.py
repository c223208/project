from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home_save')
def home_save():
    return render_template('home_save.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/calendar_medicine')
def calendar_medicine():
    return render_template('calendar_medicine.html')

@app.route('/folder')
def folder():
    return render_template('folder.html')

if __name__ == '__main__':
    app.run(debug=True)