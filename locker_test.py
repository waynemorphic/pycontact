from locker import User
import unittest

class Testuser (unittest.TestCase):
    '''
    class defining cases/methods to test the User class for its behaviours
    
    class Arguments
    TestCase class from unittest module to help create test cases
    '''

    def setUp(self):
        '''
        setUp method runs before each testing method/case
        '''

        self.new_user = User ("John", "Doe", "JDoe", "jdoe123")
        '''
        constructor creates new instance of User class before each test case/method and stores it in new_user
        '''

    def tearDown(self):
        '''
        cleans up after individual test cases/methods have ran
        '''

        User.user_list = []

## First test to check proper object initialization

    def test_init(self):
        '''
        method tests proper object initialization
        '''

        self.assertEqual(self.new_user.first_name, "John")
        self.assertEqual(self.new_user.last_name, "Doe")
        self.assertEqual(self.new_user.account_username, "JDoe")
        self.assertEqual(self.new_user.account_password, "jdoe123")

print("hello")
if __name__ ==  '__main__':
    unittest.main()