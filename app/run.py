from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    body = request.form['stuff']
    db = sql.connect('/media/peav/EXTDrive/projects/mysite/app/static/db/thedev')
    c = db.cursor()
    c.execute('''INSERT INTO submission(name, email, body) VALUES (?,?,?)''', (name, email, body))
    db.commit()
    return render_template('submit.html')

@app.route('/reader')
def reader():
    db = sql.connect('/media/peav/EXTDrive/projects/mysite/app/static/db/thedev')
    c = db.cursor()
    c.execute('''SELECT name, email, body FROM submission''')
    dblist = []
    for row in c:
        entry = [row[0],row[1],row[2]]
        dblist.append(entry)
    return render_template('reader.html', thelist=dblist)


if __name__ == '__main__':
    app.run(debug=True)
