import db as database
import os
from dotenv import load_dotenv

def login_controller(formData):
  load_dotenv()
  mongo_uri = os.getenv('MONGO_URI')
  db = database.databaseInit(mongo_uri)
  users = db.users
  username=formData['username']
  password=formData['password']
  try:
    data=users.find_one({"uname":username})
    if (data!=None):
      if data["password"]!=password:
        return "password"
      return "Loggedin"
    return "User"
  except Exception as e:
    print("ERROR Read doc:",e)
    return False