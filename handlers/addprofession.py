#!/usr/bin/env python27

import time
import datetime as dt
from datetime import datetime
import os
import webapp2
from webapp2_extras import jinja2

from google.appengine.api import users
from model.profession import Profession

class AddProfessionHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:

            values = {
                "user_logout": users.create_logout_url('/')
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("addProfessions.html", **values))

        else:

            values = {
                "login": users.create_login_url('/')
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("login.html", **values))


    def post(self):
        user = users.get_current_user()

        if user:
            title = self.request.get("title", "").strip()
            content = self.request.get("content", "").strip()
            price = self.request.get("price", "").strip()

            if(len(title) == 0 or len(content) == 0 or len(price) == 0):
                self.response.write("Debes rellenar todos los datos")
                return

            profession = Profession(user=user.user_id(), title=title, content=content, price=int(price))
            profession.put()
            time.sleep(1)
            self.redirect("/board")

        else:
            jinja = jinja2.get_jinja2(app=self.app)

            values = {
                "login": users.create_login_url('/')
            }
            self.response.write(jinja.render_template("index.html", **values))

app = webapp2.WSGIApplication([
    ('/add', AddProfessionHandler)
], debug=True)
