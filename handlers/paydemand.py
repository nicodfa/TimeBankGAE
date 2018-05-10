import time
import datetime as dt
from datetime import datetime
from google.appengine.api import users
from google.appengine.ext import ndb
import webapp2
from webapp2_extras import jinja2

from model.profession import Profession
from model.demand import Demand
from model.user import User

class PayDemandHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            id = self.request.GET['demand_id']
            demand = ndb.Key(urlsafe = id).get()

            userPay = User.query(User.id_user == demand.userDemand)
            for i in userPay:
                i.userTime -= demand.price
                i.put()
                time.sleep(1)


            userCharges = User.query(User.id_user == demand.userProf)
            for i in userCharges:
                i.userTime += demand.price
                i.put()
                time.sleep(1)


            demand.key.delete()
            time.sleep(0.5)

            self.redirect("/board")

        else:
            jinja = jinja2.get_jinja2(app=self.app)

            values = {
                "login": users.create_login_url('/')
            }
            self.response.write(jinja.render_template("index.html", **values))


app = webapp2.WSGIApplication([
    ('/pay', PayDemandHandler)
], debug=True)
