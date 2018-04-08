

class Config:
    '''
    general configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey='
  

class ProdConfig(Config):
    '''
    production configuration child class
    '''
    pass
class DevConfig(Config):
    '''
    Development Config child class
    '''
    DEBUG = True