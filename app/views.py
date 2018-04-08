from app import app
from .request import get_sources
from flask import render_template


@app.route('/')
def index():
    '''
    function returns the index page
    '''
    # newssource
    news_source = get_sources('status')
    title= "Kiptim's New's Highlight"
    
    
    return render_template('index.html', title=title, sources=news_source)
