# -*- coding: utf-8 -*-
"""
    _app_name_.stores.forms
    ~~~~~~~~~~~~~~~~~~~~~

    Store forms
"""

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import Required, Optional

__all__ = ['NewStoreForm', 'UpdateStoreForm']


class NewStoreForm(Form):
    name = StringField('Name', validators=[Required()])
    address = StringField('Address', validators=[Required()])
    city = StringField('City', validators=[Required()])
    state = StringField('State', validators=[Required()])
    zip_code = StringField('Zip Code', validators=[Required()])


class UpdateStoreForm(Form):
    name = StringField('Name', validators=[Optional()])
    address = StringField('Address', validators=[Optional()])
    city = StringField('City', validators=[Optional()])
    state = StringField('State', validators=[Optional()])
    zip_code = StringField('Zip Code', validators=[Optional()])
