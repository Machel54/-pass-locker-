import unittest 
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
        self.new_user = User("Machel","mk11")

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
        self.assertEqual(self.new_user.password,"mk11")

if __name__ == '__main__':
    unittest.main()