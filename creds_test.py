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

    def test_init(self):
      '''
      test_init checks if the object is initialised properly
      '''
      self.assertEqual(self.new_cred.account_name,"Twitter")
      self.assertEqual(self.new_cred.password,"injust2")

    


if __name__ == '__main__':
     unittest.main()