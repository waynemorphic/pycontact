
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

# Authenticate existing user details
def existing_user_authentication(username, password):
    '''
    method to authenticate the details of a registered user
    '''
    return User.authenticate_user(username, password)

# Input application name and credentials of the application
def enter_details(application, username, password):
    '''
    function to enter application name and its credentials to be stored by the application
    '''
    new_credentials = Credentials(application, username, password)
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


# Main function for running the password locker application
def main():
    print("Hello, welcome to your password locker. What is your name?")
    person_name = input()

    print(f"Hello { person_name }. What would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : reg - Register password locker account, lg - Login account if registered")
        short_code = input().lower()

        if short_code == 'reg':
            # Create account
            print("----- Register Account -----")
            print('='*30)

            print("First Name")
            f_name = input()

            print("Last Name")
            l_name = input()

            print("Account Username")
            a_username = input()

            print("Account Password")
            a_password = input()

            # Save user account details
            save_account_details(register_account(f_name, l_name, a_username, a_password))
            print('\n')
            print(f"New password locker account username is { a_username }")
            print("=" * 30)
            print('\n')

        elif short_code == 'lg':
            print("----- Login -----")
            print('='*30)

            print("Account Username")
            existing_username = input()

            print("Account Password")
            existing_password = input()

            # Authenticate the user details 
            if existing_user_authentication(existing_username, existing_password):
                print("Login Successful")
                print("=" * 30)

            print('\n')
            
            # User is successfully logged in the account
            print("What woould you like to do?")

if __name__ == '__main__':

    main()