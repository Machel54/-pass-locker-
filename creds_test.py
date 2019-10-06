import unittest
from  creds import Creds

class TestUser(unittest.TestCase):
    '''
    Test class that defines the test cases for user class
    behaviours
    '''
    def setUp(self):
      '''
      Setup method to run before each test cases
      '''
      self.new_cred = Creds("Twitter","injust2")


