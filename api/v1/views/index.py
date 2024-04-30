#!/usr/bin/python3xx
'''api status'''
import models
from models import storage
from models.base_model import BaseModel
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def returnstuff():
    '''return stuff'''
    return jsonify(status='OK')


@app_views.route('/stats')
def stuff():
    '''JSON Responses'''
    todos = {
        'states': State,
        'users': User,
        'amenities': Amenity,
        'cities': City,
        'places': Place,
        'reviews': Review
    }
    for key, value in todos.items():
        todos[key] = storage.count(value)
    return jsonify(todos)
