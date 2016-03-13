# -*- coding: utf-8 -*-
"""
    _app_name_.users
    ~~~~~~~~~~~~~~

    _app_name_ users package
"""

from ..core import Service
from .models import User


class UsersService(Service):
    __model__ = User
