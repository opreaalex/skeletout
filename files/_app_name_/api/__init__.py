# -*- coding: utf-8 -*-

from functools import wraps

from flask import jsonify
from flask_security import login_required

from ..core import OverholtError, OverholtFormError
from ..helpers import JSONEncoder
from .. import factory


def create_app(settings_override=None, register_security_blueprint=False):
    app = factory.create_app(__name__, __path__, settings_override,
                             register_security_blueprint=register_security_blueprint)

    # Set the default JSON encoder
    app.json_encoder = JSONEncoder

    return app


def route(bp, *args, **kwargs):
    kwargs.setdefault('strict_slashes', False)

    def decorator(f):
        @bp.route(*args, **kwargs)
        @login_required
        @wraps(f)
        def wrapper(*args, **kwargs):
            sc = 200
            rv = f(*args, **kwargs)
            if isinstance(rv, tuple):
                sc = rv[1]
                rv = rv[0]
            return jsonify(dict(data=rv)), sc
        return f

    return decorator
