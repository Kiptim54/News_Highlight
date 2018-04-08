import unittest
from .models import newssource
Newssource = newssource.Newssource


class NewsTest(unittest.TestCase):
    '''
    Test class to see newsource behaviour
    '''
    def setUp(self):
        '''
        setup method before every test
        '''
        self.new_newssource = Newssource("id", "BBC", "Your Trusted News Source", "#")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_newssource, Newssource))

if __name__ == '__main__':
    unittest.main()

