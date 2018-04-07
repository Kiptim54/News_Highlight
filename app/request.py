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
    get_source_url = base_url.format(api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data  = url.read()
        get_source_dict = json.loads(get_sources_data)

    #print(get_source_dict)
    source_list=[get_source_dict]
    #print(source_list)
    return get_source_dict
    
#     if get_source_dict['results']:
#         source_results_list = get_source_dict['results']
#         source_results = process_results(source_results_list)

#     return source_results
 
# def process_results(source_list):
#     source_results = []
#     for source_item in source_list:
#         name = source_item.get('name')
#         description = source_item.get('description')

#     return source_results


        
