class Creds:
  '''
  class that generates new credentials
  '''
  creds_list = []

  def __init__(self,account_name,password):
    self.account_name = account_name
    self.password = password

  def save_cred(self):
    '''
    save_cred method saves the user objects into creds_list
    '''
    Creds.creds_list.append(self)    