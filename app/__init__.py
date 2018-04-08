from flask import Flask
from .config import DevConfig
from newsapi import NewsApiClient
from flask_bootstrap import Bootstrap
 
#initialize the app
app = Flask(__name__ , instance_relative_config=True)

#setting up config
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# setting up configuration
bootstrap = Bootstrap(app)


from app import views