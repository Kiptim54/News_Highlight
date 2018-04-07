from app import app
from flask import render_template
from .request import get_sources
from newsapi import NewsApiClient

@app.route('/')
def index():
    '''
    function returns the index page
    '''
    # newssource
    news_source= get_sources('BBC')
    print(news_source)
    title= "Kiptim's New's Highlight"
    
    return render_template('index.html', title=title, sources=news_source)
