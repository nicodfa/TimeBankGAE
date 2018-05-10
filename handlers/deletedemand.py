import time
import webapp2
from webapp2_extras import jinja2

from google.appengine.api import users
from google.appengine.ext import ndb

from model.demand import Demand


class DeleteDemandHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            id = self.request.GET['demand_id']
            demand = ndb.Key(urlsafe=id).get()
            demand.key.delete()
            time.sleep(0.5)
            self.redirect("/boardDemandsAccept")

        else:

            values = {
                "login": users.create_login_url('/')
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("login.html", **values))


app = webapp2.WSGIApplication([
    ('/deleteDemand', DeleteDemandHandler)
], debug=True)