class User:
    """
    Class that generates new users
    """
    user_list = []

    def __init__(self,username,password):
      self.username = username
      self.password = password

    def save_user(self):
      '''
      save_user method saves the user objects into user_list
      '''
      User.user_list.append(self)  

    @classmethod
    def find_by_name(cls,name):
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

