from app import app
from flask import render_template

@app.route('/')
def index():
    '''
    function returns the index page
    '''
    return render_template('index.html')
