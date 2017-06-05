from __future__ import unicode_literals

from django.db import models
from mongoengine import *

# Create your models here.

class State(Document):
    state = StringField(max_length=100)
    cities = ListField(StringField(max_length=100))

    def toDATA(self):
        data = {}
        data["State"] = self.state
        data["cities"] = self.cities

    def setData(self, _state, _cities):
        self.state = _state
        self.cities = _cities

    def __unicode__(self):
        return unicode(self.state)