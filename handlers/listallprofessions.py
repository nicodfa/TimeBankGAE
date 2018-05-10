#!/usr/bin/env python27

import time
import webapp2
from webapp2_extras import jinja2

from google.appengine.api import users
from google.appengine.ext import ndb

from model.profession import Profession
from model.user import User

class ListAllProfessionsHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:

            listProfessions = Profession.query().order(-Profession.date)
            user_id = user.user_id()
            username = user.nickname()
            usersExist = User.query(User.id_user == user_id)


            if usersExist.count() == 0:
                newUser = User(id_user=user_id, username=username, userTime=5)
                newUser.put()
                time.sleep(1)

            elif usersExist.count() == 1:
                for userExist in usersExist:
                    newUser = userExist

            labels = {
                "professions": listProfessions,
                "usertb": newUser,
                "user_logout": users.create_logout_url("/")
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("boardProfession.html", **labels))

        else:

            values = {
                "login": users.create_login_url('/')
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("login.html", **values))


class ListMyProfessionsHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:

            listProfessions = Profession.query(Profession.user == user.user_id()).order(-Profession.date)

            labels = {
                "professions": listProfessions,
                "user_logout": users.create_logout_url("/")
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("myBoardProfession.html", **labels))

        else:

            values = {
                "login": users.create_login_url('/')
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("login.html", **values))


app = webapp2.WSGIApplication([
    ('/board', ListAllProfessionsHandler),
    ('/myBoard', ListMyProfessionsHandler)
], debug=True)
