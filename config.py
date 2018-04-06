import os

class Config:
    NEWS_API_BASE_URL = ''
    NEWS_API_KEY = os.environ.get('')
    SECRET_KEY = os.environ.get('')