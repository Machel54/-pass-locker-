import unittest 
import string
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.
    '''
    def setUp(self):
        '''
        Set up method to run before each test case.
        '''
        self.new_user = User("Machel","mk12")

    def tearDown(self):
        '''
        TearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly.
        '''
        self.assertEqual(self.new_user.username,"Machel")
        self.assertEqual(self.new_user.password,"mk12")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saves into the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    def test_find_user_by_name(self):
        '''
        test to check if we can find a user by name and display information
        '''
        self.new_user.save_user()
        # test_user = User("user","mk12")
        # test_user.save_user()

        found_user = User.find_by_name('Machel')

        self.assertEqual(found_user.username,self.new_user.username)

    def test_display_all_user(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(User.display_user(),User.user_list)    

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        #  test_user = User('Machel')
        #  test_user.save_user()

        user_exists = User.user_exist("Machel","jkl54")

        self.assertTrue(user_exists)

    



if __name__ == '__main__':
     unittest.main()