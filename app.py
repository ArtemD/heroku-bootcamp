from flask import Flask
from flask import render_template
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

DATABASE_URL = os.environ['DATABASE_URL']

db = create_engine(DATABASE_URL)

@app.route('/')
def index():
    results = db.execute('SELECT name FROM city')      
    return render_template('cities.html', cities=results)


@app.route('/names')
def names():
    results = db.execute('SELECT name FROM names')
    return render_template('names.html', names=results)

if __name__ == '__main__':
    app.config['DEBUG']=True
    app.run(threaded=True, port=5000)