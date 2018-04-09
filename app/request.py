import urllib.request,json
from .models import Newssource,Newsarticle


# Getting api key
api_key = None
# Getting the movie base url
base_url = None

articles_url=None
def configure_request(app):
    global api_key,base_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_url=app.config['GET_NEWS_BASE_URL']
    print(articles_url)


def get_sources(source):
    '''
    Function gets json response
    '''
    get_source_url = base_url.format("sources",api_key)
    

    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data  = url.read()
        get_source_dict = json.loads(get_sources_data)
        
        source_results = None
        if get_source_dict['sources']:
            source_results_list = get_source_dict['sources']
            source_results = process_results(source_results_list)
            
    return source_results
    

 
def process_results(source_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects
    '''
    
    source_results = []

    for source_item in source_list:
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')

        if url:
            source_object = Newssource(id,name,description,url)
            source_results.append(source_object)
    
    return source_results


def get_articles(id):
    '''
    Function responds with articles for user
    '''
    get_article_url=articles_url.format(id, api_key)
    print(get_article_url)
    

    with urllib.request.urlopen(get_article_url) as url:
        article_json=url.read()
        article_dict = json.loads(article_json)

        article_object= None

        if article_dict['articles']:
            article_list=article_dict['articles']
            article_object=process_results(article_list)
        

        return article_object
        print(article_object)
        
    def process_results(articles_list):
        '''
        Function  that processes the movie result and transform them to a list of Objects
        '''
    
        article_object = []


        for article_item in articles_list:
            id =article_item.get('id')
            title =article_item.get('title')
            author =article_item.get('author')
            description =article_item.get('description')
            url =article_item.get('url')
            publishedAt = article_item.get('publishedAt')

            if url:
                art_object = Newsarticle(id, title, author, description, url, publishedAt)
                article_object.append(art_object)

        print(article_object)
        return article_object


        
            

        # article_object = Newsarticle(id, title, author, description, url, publishedAt)
        
        # return article_object


    


        
