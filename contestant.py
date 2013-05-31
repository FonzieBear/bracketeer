from google.appengine.ext import db

class Contestant(db.Expando):
  first_name = db.StringProperty()
  last_initial = db.StringProperty()
  age = db.IntegerProperty()
  occupation = db.StringProperty()
  hometown = db.StringProperty()
  height_inches = db.IntegerProperty()
  shoe_size = db.FloatProperty()

