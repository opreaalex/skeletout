# -*- coding: utf-8 -*-

from flask_mail import Mail
from flask_mongoengine import MongoEngine
from flask_security import Security

#: Flask-MongoEngine extension instance
db = MongoEngine()

#: Flask-Mail extension instance
mail = Mail()

#: Flask-Security extension instance
security = Security()


class Dao(object):
    __model__ = None

    def _isinstance(self, model, raise_error=True):
        """Checks if the specified model instance matches the service's model.
        By default this method will raise a `ValueError` if the model is not the
        expected type.
        :param model: the model instance to check
        :param raise_error: flag to raise an error on a mismatch
        """
        rv = isinstance(model, self.__model__)
        if not rv and raise_error:
            raise ValueError('%s is not of type %s' % (model, self.__model__))
        return rv

    def _preprocess_params(self, kwargs):
        """Returns a preprocessed dictionary of parameters. Used by default
        before creating a new instance or updating an existing instance.
        :param kwargs: a dictionary of parameters
        """
        kwargs.pop('csrf_token', None)
        return kwargs

    def save(self, model):
        """Commits the model to the database and returns the model
        :param model: the model to save
        """
        self._isinstance(model)
        return model.save()

    def all(self):
        """Returns a generator containing all instances of the service's model.
        """
        return self.__model__.objects.all()

    def get(self, obj_id):
        """Returns an instance of the service's model with the specified id.
        Returns `None` if an instance with the specified id does not exist.
        :param id: the instance id
        """
        return self.__model__.objects.get(id=obj_id)

    def get_all(self, *obj_ids):
        """Returns a list of instances of the service's model with the specified
        ids.
        :param *ids: instance ids
        """
        return self.__model__.objects.filter(id__in=obj_ids)

    def find(self, **kwargs):
        """Returns a list of instances of the service's model filtered by the
        specified key word arguments.
        :param **kwargs: filter parameters
        """
        return self.__model__.objects.filter(**kwargs)

    def first(self, **kwargs):
        """Returns the first instance found of the service's model filtered by
        the specified key word arguments.
        :param **kwargs: filter parameters
        """
        return self.find(**kwargs).first()

    def get_or_none(self, obj_id):
        """Returns an instance of the service's model with the specified id or
        raises an 404 error if an instance with the specified id does not exist.
        :param id: the instance id
        """
        return self.first(**{'id': obj_id})

    def new(self, **kwargs):
        """Returns a new, unsaved instance of the service's model class.
        :param **kwargs: instance parameters
        """
        return self.__model__(**self._preprocess_params(kwargs))

    def create(self, **kwargs):
        """Returns a new, saved instance of the service's model class.
        :param **kwargs: instance parameters
        """
        return self.new(**kwargs).save()

    def update(self, model, **kwargs):
        """Returns an updated instance of the service's model class.
        :param model: the model to update
        :param **kwargs: update parameters
        """
        self._isinstance(model)
        model.update(**kwargs)
        return model

    def delete(self, model):
        """Immediately deletes the specified model instance.
        :param model: the model instance to delete
        """
        self._isinstance(model)
        model.delete()

