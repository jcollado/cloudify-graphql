# -*- coding: utf-8 -*-

"""Application module."""

import graphene

from flask import Flask
from flask_graphql import GraphQLView

from cloudify_graphql.query import Query


def create_app():
    """Create flask application."""
    app = Flask(__name__)

    schema = graphene.Schema(query=Query)
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True),
    )

    return app
