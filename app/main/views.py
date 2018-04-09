from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources, get_articles
from flask import render_template



@main.route('/')
def index():
    '''
    function returns the index page
    '''
    # newssource
    news_source = get_sources('status')
    title= "Kiptim's New's Highlight"
    
    
    return render_template('index.html', title=title, sources=news_source)

@main.route('/articles/<id>')
def articles(id):
    '''
    '''
    articles_get=get_articles(id)
    title= "Articles"

    return render_template('articles.html', title=title , articles=articles_get)
