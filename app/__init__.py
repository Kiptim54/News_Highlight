from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    #app configurations
    app.config.from_object(config_options[config_name])

    #initialize extensions
    bootstrap.init.app(app)





