import unittest  
from  credentials import Credential
from user import User

class TestCredential(unittest.TestCase):
    '''
    Test class that defines the test cases for user class
    behaviours
    '''

    def setUp(self):
      '''
      Setup method to run before each test cases
      '''
      self.new_credential = Credential("Machel","mk12")

    def test_init(self):
       '''
       test_init checks if the object is initialised properly
       '''
       self.new_credential.username, ("Machel")
       self.new_credential.password, ("mk12")

    def tearDown(self):
       '''
        TearDown method that does clean up after each test case has run.
       '''
       Credential.credential_list = []

    def test_save_credential(self):
       '''
       test_save_credential tests if a new credential has been added to the credential_list 
       '''
       self.new_credential.save_credential()
       self.assertEqual(len(Credential.credential_list),1)

    def test_display_credential(self):
       '''
       test to display the credentials
       '''
       self.new_credential.save_credential()
       self.assertEqual(Credential.display_credential('username'),Credential.credential_list)


   #  def test_delete_credential(self):
   #     '''
   #     test_delete_contact to test if we can remove a password from our credentials
   #     '''
   #     self.new_credential.save_credential()
   #     test_credential = ("Test","user","mk12")
   #    #  test_credential.save_credential()

   #     self.new_credential.delete_credential()
   #    #  self.assertEqual(len(Credential.credential_list),1)

  

if __name__ == '__main__':
     unittest.main() 
           