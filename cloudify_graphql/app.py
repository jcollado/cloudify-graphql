# -*- coding: utf-8 -*-

"""Application module."""

from flask import Flask


def create_app():
    """Create flask application."""
    app = Flask(__name__)
    return app
