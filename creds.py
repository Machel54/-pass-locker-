class Creds:
  '''
  class that generates new credentials
  '''
  creds_lists = []

  def __init__(self,account_name,password):
    self.account_name = account_name
    self.password = password