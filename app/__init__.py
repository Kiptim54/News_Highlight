from flask import Flask
from .config import DevConfig
from newsapi import NewsApiClient
 
#initialize the app
app = Flask(__name__ , instance_relative_config=True)

#setting up config
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')
newsapi = NewsApiClient(api_key='966c0d049ee74558b04995ae6d4d3b30')
sources = newsapi.get_sources()
from app import views