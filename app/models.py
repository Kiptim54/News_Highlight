class Newssource:
    '''
    Newssource class to define source objects
    '''
    def __init__(self, id, name, description, url):
        self.id= id
        self.name = name
        self.description = description
        self.url = url

class Newsarticle:
    '''
    Newsarticles class that define article objects
    '''

    def __init__(self, id, title, author, description, urlToImage, url, publishedAt):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.urlToImage = urlToImage
        self.url = url
        self.publishedAt=publishedAt