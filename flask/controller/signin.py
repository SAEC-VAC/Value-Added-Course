import db as database
import os
from dotenv import load_dotenv

def signin_controller(formData):
  load_dotenv()
  mongo_uri = os.getenv('MONGO_URI')
  db = database.databaseInit(mongo_uri)
  users = db.users
  email = formData['email']
  uname = formData['uname']
  try:
    checkExistingUser = users.find_one({'email':email})
    if(checkExistingUser == None):
      checkUsername = users.find_one({'uname':uname})
      if(checkUsername == None):
        users.insert_one(formData)
        return 'inserted'
      return 'username'
    return 'email'
  except Exception as e:
      print("An Exception Occured, Read Docs:: ", e)
      return 'error'