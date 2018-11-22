import unittest
from models import blog
Blog = blog.Blog

class BlogTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Blog class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_blog = Movie()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blog))


if __name__ == '__main__':
    unittest.main()
