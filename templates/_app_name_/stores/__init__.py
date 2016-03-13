# -*- coding: utf-8 -*-
"""
    _app_name_.stores
    ~~~~~~~~~~~~~~~

    _app_name_ stores package
"""

from ..core import Service, _app_upper_name_Error
from .models import Store


class StoresService(Service):
    __model__ = Store

    def add_manager(self, store, user):
        if user in store.managers:
            raise _app_upper_name_Error(u'Manager exists')
        store.managers.append(user)
        return self.save(store), user

    def remove_manager(self, store, user):
        if user not in store.managers:
            raise _app_upper_name_Error(u'Invalid manager')
        store.managers.remove(user)
        return self.save(store), user

    def add_product(self, store, product):
        if product in store.products:
            raise _app_upper_name_Error(u'Product exists')
        store.products.append(product)
        return self.save(store)

    def remove_product(self, store, product):
        if product not in store.products:
            raise _app_upper_name_Error(u'Invalid product')
        store.products.remove(product)
        return self.save(store)
