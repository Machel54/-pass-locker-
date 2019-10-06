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

    def tearDown(self):
      '''
       TearDown method that does clean up after each test case has run.
      '''
      Creds.creds_list = []

    def test_save_cred(self):
      '''
      test_save_cred tests if a new credential has been added to the creds_list 
      '''
      self.new_cred.save_cred()
      self.assertEqual(len(Creds.creds_list),1)


if __name__ == '__main__':
     unittest.main()