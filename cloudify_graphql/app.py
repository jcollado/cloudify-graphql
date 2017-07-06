# -*- coding: utf-8 -*-

"""Application module."""

import graphene

from flask import Flask
from flask_graphql import GraphQLView

from config import config
from cloudify_graphql.query import Query
from cloudify_graphql.mutation import Mutation


def create_app(config_name):
    """Create flask application."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    schema = graphene.Schema(query=Query, mutation=Mutation)
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True),
    )

    return app
