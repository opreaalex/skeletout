# -*- coding: utf-8 -*-

from ..core import db
from ..helpers import JsonSerializer


class Example(db.Document):
    name = db.StringField(required=True)

