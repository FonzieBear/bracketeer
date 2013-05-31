import os
import urllib

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import ndb

import gambler

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'])

class MainPage(webapp2.RequestHandler):

    def get(self):
      user = users.get_current_user()
      user_id = user.user_id()

      gambler_key = db.Key.from_path('Gambler', user_id)
      gambler_obj = db.get(gambler_key)

      if not gambler_obj:
        gambler_obj = gambler.Gambler(
            key_name=user_id, user_id=user_id, user_obj=user)
        gambler_obj.put()

      print gambler_obj
      template_values = {
          'first_name': gambler_obj.first_name,
          'last_name': gambler_obj.last_name,
          'nickname': user.nickname()}

      template = JINJA_ENVIRONMENT.get_template('templates/main.html')
      self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([('/', MainPage),], debug=True)

