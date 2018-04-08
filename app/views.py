from flask import render_template
from app import app
from .request import get_sources
#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    status_sources = get_sources('status')
    title= "Kiptim's New's Highlight"
    return render_template('index.html', title = title, status = status_sources)



