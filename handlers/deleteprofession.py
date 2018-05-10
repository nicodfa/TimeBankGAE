import time

from google.appengine.api import users
from google.appengine.ext import ndb
from model.profession import Profession
from model.demand import Demand

import webapp2
from webapp2_extras import jinja2

class DeleteProfessionHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            id = self.request.GET['profession_id']
            profession = ndb.Key(urlsafe = id).get()

            if user.user_id() == profession.user:
                demands = Demand.query(Demand.profession_id == id)
                if demands.count() > 0:
                    for i in demands:
                        i.key.delete()
                        time.sleep(0.5)

                profession.key.delete()
                time.sleep(0.5)
                self.redirect("/board")
        else:

            values = {
                "login": users.create_login_url('/')
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("login.html", **values))

app = webapp2.WSGIApplication([
    ('/delete', DeleteProfessionHandler)
], debug=True)
