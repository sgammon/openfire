# -*- coding: utf-8 -*-
## Project Models Init

from google.appengine.ext import ndb
from google.appengine.ext.ndb import model


class Person(model.Model):

    firstname = ndb.StringProperty()
    lastname = ndb.StringProperty()
    dob = ndb.DateProperty()
