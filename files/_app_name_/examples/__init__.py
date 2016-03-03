# -*- coding: utf-8 -*-

from ..core import Dao
from .models import Example


class ExamplesDao(Dao):
    __model__ = Example

    def __init__(self, *args, **kwargs):
        super(ExamplesDao, self).__init__(*args, **kwargs)
        # Do any extra initialization

    def _preprocess_params(self, kwargs):
        kwargs = super(ProductsService, self)._preprocess_params(kwargs)
        # Do any extra paramter changes before persisting
        return kwargs

