import unittest
from app.models import Newsarticle
class NewsTest(unittest.TestCase):
    '''
    Test class to see newsource behaviour
    '''
    def setUp(self):
        '''
        setup method before every test
        '''
        self.new_newsarticle = Newsarticle("id", "Shares in sanctions-hit Russian firms crash", "Brenda Kiptim", "who knows","#","5pm")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_newsarticle, Newsarticle))

if __name__ == '__main__':
    unittest.main()
