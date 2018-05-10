
from google.appengine.ext import ndb

class Demand(ndb.Model):
    date = ndb.DateTimeProperty(auto_now=True, indexed=True)
    profession_id = ndb.StringProperty(required=True, indexed=True)
    profession = ndb.StringProperty(required=True, indexed=True)
    userProf = ndb.StringProperty(required=True, indexed=True)
    userDemand = ndb.StringProperty(required=True, indexed=True)
    price = ndb.IntegerProperty(required=True, indexed=True)
    accepted = ndb.BooleanProperty()
