
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

# Application exists
def found_existing_application(platform):
    '''
    function to verify whether a platform has been registered or not
    '''
    return Credentials.existing_platform(platform)

# Display credentials
def display_credentials():
    '''
    function to view credentials stored in the application
    '''
    
    return Credentials.view_credentials()

# Generate a password
def random_password():
    '''
    function to generate a random password from PasswordGenerator module
    '''
    return Credentials.generate_password()


# Main function for running the password locker application
def main():
    print("\n")
    print("Hello, welcome to your password locker. What is your name?")
    person_name = input()

    print("\n")
    print(f"Hello { person_name }. What would you like to do?")
    print('\n')

    while True:
        print("""Use these short codes : 
        reg - Register password locker account
        lg - Login account if registered
        ex - exit the application
        """)
        short_code = input().lower()

        if short_code == 'reg':
            # Create account
            print('='*80)
            print("----- Register Account -----")
            print('='*80)

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
            print("=" * 80)
            print(f"New password locker account username is { a_username }") 
            print("Type lg to Login to your new Password Locker account")
            print("=" * 80)
            print('\n')

        elif short_code == 'lg':
            print('='*80)
            print("----- Login -----")
            print('='*80)

            print("Account Username")
            existing_username = input()

            print("Account Password")
            existing_password = input()

            # Authenticate the user details 
            if existing_user_authentication(existing_username, existing_password):
                print("=" * 80)
                print("Login Successful")
                print("=" * 80)

                print('\n')
            
                # User is successfully logged in the account
                print("What would you like to do?")
                print('\n')

                while True:
                    print("""Use these short codes to use the features of password locker : 
                    rp - register platform
                    search - search for a platform
                    vc - view existing applications and their credentials
                    del - delete a platform and its credentials
                    lo - log out""")
                    entry_code = input()

                    # Entering platfrom specific credentials
                    if entry_code == 'rp':
                        print("\n")
                        print("=" * 80)
                        print("-----Create Platform Account-----")
                        print("=" * 80)
                        
                        print("Name of Platform")
                        n_platform = input().strip().capitalize() #remove any white spaces 

                        print("Platform Username")
                        u_platform = input().capitalize()

                        print("Platform Password")
                        print("Can we generate a password for you? Y/N")
                        opt_password = input().capitalize()

                        while True:
                            if opt_password == "N":
                                print("Enter your own password")
                                p_password = input()

                            elif opt_password == "Y":
                                p_password = random_password()

                            break # break the while loop

                        # Saving platfrom credentials
                        save_application_credentials(enter_details(n_platform, u_platform, p_password))
                        print("=" * 80)
                        print(f"Credentials for { n_platform } have been saved successfully")
                        print("=" * 80)
                    
                    # Search for an existing application by name
                    elif entry_code == "search": 
                        print("\n")
                        print("=" * 80)
                        print("-----Name of application to search-----")
                        s_query = input().strip().capitalize()
                        print("=" * 80)

                        while True:
                            # Successful search query
                            if found_existing_application(s_query):
                                # find_application = search_application(s_query)
                                print("\n")
                                print("=" * 80)
                                print(f"{ s_query } has been registered in password locker")
                                print("=" * 80)
                            # Unsuccessful search query
                            else:
                                print("\n")
                                print("=" * 80)
                                print(f"{s_query} has not been registered in password locker")
                                print("=" * 80)
                            break
                    
                    # View applications and credentials
                    elif entry_code == "vc":                        
                        if display_credentials():
                            print("\n")
                            print("=" * 80)
                            print("Here are the applications and their respective credentials")
                            for credential in display_credentials():
                                print(f"Platform : { credential.platform } Username : { credential.username } Password: { credential.password }")
                            print("=" * 80)
                            
                        # Unavailable application
                        else:
                            print("\n")
                            print("=" * 80)
                            print("You do not have any registered platforms")
                            print("=" * 80)

                    elif entry_code == "del":
                        print("=" * 80)
                        print("Platforms saved")
                        for credential in display_credentials():
                                print(f"Platform : { credential.platform } Username : { credential.username } Password: { credential.password }")
                        print("=" * 80)

                        print("\n")
                        print("=" * 80)
                        print("-----Enter name of platfrom to delete-----")
                        del_application = input().strip().capitalize()
                        print("=" * 80)

                        if found_existing_application(del_application):
                            while True:
                                print(f"Delete { del_application }? Y/N")
                                del_answer = input().capitalize()

                                if del_answer == "Y":
                                    delete_application_credentials(search_application(del_application))
                                    print("=" * 80)
                                    print(f"{ del_application } has been deleted successfully")
                                    print("=" * 80)
                                elif del_answer == "N":
                                    print(f"{ del_application } has not been deleted")

                                else:
                                    print("=" * 80)
                                    print("Invalid entry!")
                                    print("=" * 80)
                                break

                    elif entry_code == "lo":
                        print("=" * 80)
                        print("Logged out successfully")
                        print("=" * 80)
                        break #added break since after logging out keeps looping


                    else:
                        print("=" * 80)
                        print("Invalid short code entry!")
                        print("=" * 80)
                    # break
                    # continue
            

            else:
                print("=" * 80)
                print("Invalid username or password!")
                print("=" * 80)
        elif short_code == 'ex':
            print("\n ")
            print("Bye..")
            break
        else:
            print("Sorry, please try again")
        # continue
        #break

if __name__ == '__main__':

    main()