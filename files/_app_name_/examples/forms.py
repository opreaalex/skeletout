# -*- coding: utf-8 -*-

from flask_wtf import Form, TextField, SelectMultipleField, Required

__all__ = ['NewExampleForm', 'UpdateExampleForm']


class NewExampleForm(Form):
    name = TextField('Name', validators=[Required()])


class UpdateProductForm(ProductFormMixin, Form):
    name = TextField('Name', validators=[Required()])

