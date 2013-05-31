from google.appengine.ext import db

class Gambler(db.Model):
  first_name = db.StringProperty()
  last_name = db.StringProperty()
  user_obj = users.User()

