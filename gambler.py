from google.appengine.api import users
from google.appengine.ext import db

class Gambler(db.Model):
  first_name = db.StringProperty()
  last_name = db.StringProperty()
  user_id = db.StringProperty()
  user_obj = users.User()
  is_admin = db.BooleanProperty(default=False)

