class User:
    """
    Class that generates new users
    """
    user_list = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user(self):
        '''
        save_user method saves the user objects into user_list
        '''
        User.user_list.append(self)

    @classmethod
    def find_by_name(cls, name):
        '''
        Method that takes in a name and returns a the name that matches that username.
        Args:
          name: name to search for
        Returns :
        name of person that matches the username.
        '''

        for user in cls.user_list:
            if user.username == name:
                return user

    @classmethod
    def display_user(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list

    @classmethod
    def user_exist(cls, name, password):
        '''
        Method that checks if a user exists from the user list.
        Args:
            name: username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        the_user = ""
        for user in User.user_list:
            if (user.username == name and user.password == password):
                the_user = user.username
        return the_user