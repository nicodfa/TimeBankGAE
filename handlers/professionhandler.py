
from google.appengine.api import users
from google.appengine.ext import ndb

from model.profession import Profession
from model.user import User

import webapp2
from webapp2_extras import jinja2

class ProfessionHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            id = self.request.GET['profession_id']
            profession = ndb.Key(urlsafe = id).get()
            user_id = user.user_id()
            time = User.query(User.id_user == user_id).fetch(projection=[User.userTime])

            labels = {
                "profession": profession,
                "userTime": time
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("professionView.html", **labels))

        else:
            jinja = jinja2.get_jinja2(app=self.app)

            values = {
                "login": users.create_login_url('/')
            }
            self.response.write(jinja.render_template("index.html", **values))


app = webapp2.WSGIApplication([
    ('/profession', ProfessionHandler)
], debug=True)
