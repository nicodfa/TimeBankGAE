#!/usr/bin/env python27

from google.appengine.ext import ndb

class User(ndb.Model):
    id_user = ndb.StringProperty(required=True, indexed=True)
    username = ndb.StringProperty(required=True, indexed=True)
    userTime = ndb.IntegerProperty(required=True, indexed=True)
