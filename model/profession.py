#!/usr/bin/env python27

from google.appengine.ext import ndb

class Profession(ndb.Model):
    date = ndb.DateTimeProperty(auto_now=True, indexed=True)
    user = ndb.StringProperty(required=True, indexed=True)
    title = ndb.StringProperty(required=True, indexed=True)
    content = ndb.StringProperty(required=True, indexed=True)
    price = ndb.IntegerProperty(required=True, indexed=True)
