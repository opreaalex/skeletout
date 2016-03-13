# -*- coding: utf-8 -*-
"""
    _app_name_.frontend.assets
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    frontend application asset "pipeline"
"""

from flask_assets import Environment, Bundle


#: application css bundle
css__app_name_ = Bundle("less/_app_name_.less",
                   filters="less", output="css/_app_name_.css",
                   debug=False)

#: consolidated css bundle
css_all = Bundle("css/bootstrap.min.css", css__app_name_,
                 "css/bootstrap-responsive.min.css",
                 filters="cssmin", output="css/_app_name_.min.css")

#: vendor js bundle
js_vendor = Bundle("js/vendor/jquery-1.10.1.min.js",
                   "js/vendor/bootstrap-2.3.3.min.js",
                   "js/vendor/underscore-1.4.4.min.js",
                   "js/vendor/backbone-1.0.0.min.js",
                   filters="jsmin", output="js/vendor.min.js")

#: application js bundle
js_main = Bundle("coffee/*.coffee", filters="coffeescript", output="js/main.js")


def init_app(app):
    webassets = Environment(app)
    webassets.register('css_all', css_all)
    webassets.register('js_vendor', js_vendor)
    webassets.register('js_main', js_main)
    webassets.manifest = 'cache' if not app.debug else False
    webassets.cache = not app.debug
    webassets.debug = app.debug
