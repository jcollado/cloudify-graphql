# -*- coding: utf-8 -*-

"""Main module."""

import os

from cloudify_graphql.app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
