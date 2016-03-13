# -*- coding: utf-8 -*-
"""
    manage
    ~~~~~~

    Manager module
"""

from flask_script import Manager

from _app_name_.api import create_app
from _app_name_.manage import CreateUserCommand, DeleteUserCommand, ListUsersCommand

manager = Manager(create_app())
manager.add_command('create_user', CreateUserCommand())
manager.add_command('delete_user', DeleteUserCommand())
manager.add_command('list_users', ListUsersCommand())

if __name__ == "__main__":
    manager.run()
