class Credential:
  '''
  class that generates new credentials
  '''
  credential_list = []

  def __init__(self,username,password):
    self.username = username
    self.password = password

  def save_credential(self):
    '''
    save_cred method saves the user objects into creds_list
    '''
    Credential.credential_list.append(self)

  @classmethod
  def display_credential(cls, username):
          '''
          method that returns the user list
          '''
          return cls.credential_list 
  def delete_credential(self):
    '''
    delete_contact method deletes a saved credential from the credential_list
    '''
    Credential.credential_list.remove(self)

 


