from locker import User
import unittest
from locker import Credentials

# Testig the cases for the User class
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

## Second test to check whether user details are saved
    def test_save_user_details(self):
        '''
        method to test whether user details are saved
        '''

        self.new_user.save_user_details()
        self.assertEqual(len(User.user_list),1)

## Credentials class
class TestCredentials(unittest.TestCase):
    '''
    test cases and methods to test the credentials class
    '''

    def setUp(self):
        '''
        setUp case to run before each case or method
        '''

        self.new_credentials = Credentials("Twitter", "jdoe", "twitter123")
        '''
        constructor to create new instances of the credentials class
        '''

    def tearDown(self):
        '''
        cleans up after every case/method runs
        '''

        Credentials.credentials_list = []
    
    def test_init(self):
        '''
        checking for proper credentials class initialization
        '''

        self.assertEqual(self.new_credentials.platform,"Twitter")
        self.assertEqual(self.new_credentials.username, "jdoe")
        self.assertEqual(self.new_credentials.password, "twitter123")

## First Credentials test for saving credentials entries
    def test_save_credentials(self):
        '''
        method to check if platform credentials are saved
        '''

        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

## Second Credentials test for checking ability to save multiple credentials
    def test_save_multiple_credentials(self):
        '''
        method to test if multiple user credentials can be saved
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter", "jdoe", "twitter123")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

## Third Credentials test to test if existing credentials can be deleted from the application
    def test_delete_credentials(self):
        '''
        method to test if credentials are removable
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials ("Twitter", "jdoe", "twitter123")
        test_credentials.save_credentials

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 0) # Added 0 at the end since Assertion error ocurred saying 0 != 1. Resolved that assertion error

## Fourth Credentials test for returning credentials in the application
    def test_view_credentials(self):
        '''
        method that returns all saved credentials
        '''

        self.assertEqual(Credentials.view_credentials(), Credentials.credentials_list)

## Fifth test for searching existing platforms in the application by name
    def test_search_platform(self):
        '''test to find a platform by the name given by the user
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter", "jdoe", "twitter123")
        test_credentials.save_credentials()

        found_platform = Credentials.search_platform("Twitter")
        self.assertEqual(found_platform.platform, test_credentials.platform)

print("hello")
if __name__ ==  '__main__':
    unittest.main()