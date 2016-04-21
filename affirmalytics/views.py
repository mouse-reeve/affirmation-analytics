''' views and routing '''
from flask import render_template

from affirmalytics import app

@app.route('/')
def index():
    ''' render the home page '''
    return render_template('index.html')
