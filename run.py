#! usr/bin/env python3.8
'''
#! shebang code that makes the script executable without necessarily typing python3.8

 To execute the program, we type on the terminal chmod +x run.py
'''
from locker import User
from locker import Credentials
from password_generator import PasswordGenerator

# Input user details
def register_account(fname, lname, uname, psword):
    '''
    function that registers the user into the password locker application
    '''
    new_user = User(fname, lname, uname, psword)
    return new_user

# Save user details
def save_account_details(details):
    '''
    function to save account registration details 
    '''
    details.save_user_details()

# Input application name and credentials of the application
def enter_details(application, usernme, passwrd):
    '''
    function to enter application name and its credentials to be stored by the application
    '''
    new_credentials = Credentials(application, usernme, passwrd)
    return new_credentials

# Save application credentials
def save_application_credentials(credentials):
    '''
    function to save application credentials entered by the user
    '''
    credentials.save_credentials()

# Delete an application and its credentials
def delete_application_credentials(credentials):
    '''
    function to delete application credentials
    '''
    credentials.delete_credentials()

# Search for an existing application by name
def search_application(platform):
    '''
    function to search for an existing application
    '''

    return Credentials.search_platform(platform)

# Display credentials
def display_credentials():
    '''
    function to view credentials stored in the application
    '''
    
    return Credentials.view_credentials()

# Generate a password
def random_password(password):
    '''
    function to generate a random password from PasswordGenerator module
    '''
    return Credentials.generate_password(password)