class User:
    '''
    Defines the user details. 
    '''

    user_list = []
    '''
    An empty list that stores user details
    '''

    def __init__(self, first_name, last_name, account_username, account_password):
        '''
        constructor takes in arguments that declare the user personal details
        and the password locker account credentials
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.account_username = account_username
        self.account_password = account_password
        '''
        instance variables unique to the new instance of the class
        '''

    def save_user_details(self):
        '''
        method to save user details
        '''
        User.user_list.append(self)