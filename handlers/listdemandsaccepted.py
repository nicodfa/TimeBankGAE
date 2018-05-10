#!/usr/bin/env python27



import webapp2
from webapp2_extras import jinja2

from google.appengine.api import users
from google.appengine.ext import ndb

from model.demand import Demand
from model.user import User


class ListDemandsAcceptedHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            listDemands = Demand.query().order(-Demand.date)
            user_id=user.user_id()
            userst = User.query(User.id_user == user_id).fetch(projection=[User.userTime])
            time = 0
            for u in userst:
                time = u.userTime

            labels = {
                "demands": listDemands,
                "user": user,
                "userTime": int(time),
                "user_logout": users.create_logout_url("/")
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("boardDemandsAccept.html", **labels))
        else:

            values = {
                "login": users.create_login_url('/')
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("login.html", **values))


app = webapp2.WSGIApplication([
    ('/boardDemandsAccept', ListDemandsAcceptedHandler)
], debug=True)
