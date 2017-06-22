# -*- coding: utf-8 -*-

"""Loader package."""

import requests

from flask import (
    current_app as app,
    g,
    request,
)


class Loader(object):

    """Loader."""

    DEFAULT_PARAMS = {}

    def __init__(self):
        self.cache = {}

    @classmethod
    def get(cls):
        if cls.__name__ not in g:
            instance = cls()
            setattr(g, cls.__name__, instance)

        return getattr(g, cls.__name__)

    def load(self, params=None):
        """Get data from cache or by querying the REST API."""
        if params is None:
            params = {}
        params.update(self.DEFAULT_PARAMS)
        key = tuple(params.items())
        if key in self.cache:
            return self.cache[key]

        items = self.load_from_rest(params)

        self.cache[key] = items
        return items

    def load_from_rest(self, params):
        """Get data by querying the REST API."""
        url = (
            'http://{}/api/v3/{}'
            .format(app.config['MANAGER_IP'], self.ENDPOINT)
        )
        headers = {
            'Authorization': request.headers['Authorization'],
            'Tenant': request.headers['Tenant'],
        }
        response = requests.get(
            url,
            headers=headers,
            params=params,
        )
        items = [
            self.model_cls.from_rest(item_data)
            for item_data
            in response.json()['items']
        ]
        return items
