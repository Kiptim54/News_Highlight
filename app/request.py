from app import app
import urllib.request,json
from .models import newssource
from newsapi import NewsApiClient


Newssource = newssource.Newssource

# access the api  key
api_key = app.config['NEWS_API_KEY']

# news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_sources(source):
    '''
    Function gets json response
    '''
    get_source_url = base_url + api_key

    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data  = url.read()
        get_source_dict = json.loads(get_sources_data)

        source_list=[get_source_dict]
        print(source_list)
    return source_list
   
        

#         source_results = None
#         if get_source_dict['sources']:
#             source_results_list = get_source_dict['sources']
#             source_results = process_results(source_results_list)
#     print(source_results)
#     return source_results
    
#     print(source_results_list)
 
# def process_results(source_list):
#     '''
#     Function  that processes the movie result and transform them to a list of Objects
#     '''
    
#     source_results = []
#     for source_item in source_list:
#         name = source_item.get('name')
#         description = source_item.get('description')
#         url = source_item.get('url')

#     return source_results
    


    


        
