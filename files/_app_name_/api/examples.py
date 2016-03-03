# -*- coding: utf-8 -*-

from flask import Blueprint, request

from ..forms import NewExampleForm, UpdateExampleForm
from ..dao import examples
from . import route

bp = Blueprint('examples', __name__, url_prefix='/examples')


@route(bp, '/')
def list():
    examples_dto = {'data': [
        {'id': str(e.id), 'name': e.name}
    ]}
    return examples_dto


@route(bp, '/', methods=['POST'])
def create():
    form = NewProductForm()
    if form.validate_on_submit():
	example = examples.create(**request.json)
	example_dto = {'data': {
            'id': str(example.id),
            'name': example.name
        }}
        return example_dto
    return {'error': 'Unable to create a new example'}


@route(bp, '/<example_id>')
def show(example_id):
    example = examples.get(example_id)
    example_dto = {'data': {
        'id': str(example.id),
        'name': example.name
    }}
    return example_dto


@route(bp, '/example_id>', methods=['PUT'])
def update(example_id):
    form = UpdateExampleForm()
    if form.validate_on_submit():
        example = examples.update(examples.get(example_id), **request.json)
	example_dto = {'data': {
            'id': str(example.id),
            'name': example.name
        }}
        return example_dto
    return {'error': 'Unable to update example'}


@route(bp, '/<example_id>', methods=['DELETE'])
def delete(example_id):
    examples.delete(examples.get(example_id))
    return None, 204

