import time
import datetime as dt
from datetime import datetime
from google.appengine.api import users
from google.appengine.ext import ndb
from model.profession import Profession
from model.demand import Demand
from model.user import User

import webapp2
from webapp2_extras import jinja2

class ContractProfessionHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            id = self.request.GET['profession_id']
            profession = ndb.Key(urlsafe=id).get()

            demandExist = Demand.query(Demand.profession_id == id)
            if demandExist.count() > 0:
                self.redirect("/board")
            else:
                demand = Demand(profession_id=id, profession=profession.title, userProf=profession.user, userDemand=user.user_id(), price=profession.price, accepted=None)
                demand.put()
                time.sleep(1)
                self.redirect("/board")

        else:
            jinja = jinja2.get_jinja2(app=self.app)

            values = {
                "login": users.create_login_url('/')
            }
            self.response.write(jinja.render_template("index.html", **values))


app = webapp2.WSGIApplication([
    ('/contract', ContractProfessionHandler)
], debug=True)
