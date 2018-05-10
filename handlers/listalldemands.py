#!/usr/bin/env python27

import time
import webapp2
from webapp2_extras import jinja2

from google.appengine.api import users
from google.appengine.ext import ndb

from model.demand import Demand


class ListAllDemandsHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            listDemands = Demand.query().order(Demand.date)

            labels = {
                "demands": listDemands,
                "user": user,
                "user_logout": users.create_logout_url("/")
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("boardDemands.html", **labels))
        else:

            values = {
                "login": users.create_login_url('/')
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("login.html", **values))


class DemandAcceptHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            id = self.request.GET['demand_id']
            demand = ndb.Key(urlsafe = id).get()
            demand.accepted = True
            demand.put()
            time.sleep(1)
            self.redirect("/board")

        else:
            values = {
                "login": users.create_login_url('/')
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("login.html", **values))


class DemandRefuseHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            id = self.request.GET['demand_id']
            demand = ndb.Key(urlsafe = id).get()
            demand.accepted = False
            demand.put()
            time.sleep(1)
            self.redirect("/board")

        else:
            values = {
                "login": users.create_login_url('/')
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("login.html", **values))


app = webapp2.WSGIApplication([
    ('/boardDemands', ListAllDemandsHandler),
    ('/demandAccept', DemandAcceptHandler),
    ('/demandRefuse', DemandRefuseHandler)
], debug=True)
