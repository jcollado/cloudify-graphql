# -*- coding: utf-8 -*-

"""Application module."""

import graphene

from flask import Flask
from flask_graphql import GraphQLView


class Query(graphene.ObjectType):
    """Main GraphQL query."""
    ping = graphene.String()

    def resolve_ping(self, args, context, info):
        """Return ping response."""
        return 'pong'


def create_app():
    """Create flask application."""
    app = Flask(__name__)

    schema = graphene.Schema(query=Query)
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True),
    )

    return app
