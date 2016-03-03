# -*- coding: utf-8 -*-

from flask_script import Manager

from _app_name_.api import create_app

manager = Manager(create_app())
# manager.add_command('example', ExampleFlaskScriptCommand())

if __name__ == "__main__":
    manager.run()

