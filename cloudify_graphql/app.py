# -*- coding: utf-8 -*-

"""Application module."""

import graphene
import requests

from flask import Flask
from flask_graphql import GraphQLView
from requests.auth import HTTPBasicAuth

MANAGER_IP = '172.20.0.2'
TENANT = 'default_tenant'
USER = 'admin'
PASSWORD = 'admin'


class Tenant(graphene.ObjectType):
    """A tenant."""
    name = graphene.String(description='Tenant name')
    groups = graphene.Int(description='Group count')
    users = graphene.Int(description='User count')

    def resolve_name(self, args, context, info):
        """Get tenant name."""
        return self.name

    def resolve_groups(self, args, context, info):
        """Get tenant group count."""
        return self.groups

    def resolve_users(self, args, context, info):
        """Get tenant user count."""
        return self.users


class Query(graphene.ObjectType):
    """Main GraphQL query."""
    ping = graphene.String(description='Check API status')
    tenants = graphene.List(
        Tenant,
        description='Cloudify tenants.',
    )

    def resolve_ping(self, args, context, info):
        """Return ping response."""
        return 'pong'

    def resolve_tenants(self, args, context, info):
        """Get list of tenants."""
        url = 'http://{}/api/v3/tenants'.format(MANAGER_IP)
        headers = {
            'Tenant': TENANT,
        }
        response = requests.get(
            url,
            auth=HTTPBasicAuth(USER, PASSWORD),
            headers=headers,
        )
        tenants = [
            Tenant(**tenant_data)
            for tenant_data
            in response.json()['items']
        ]
        return tenants


def create_app():
    """Create flask application."""
    app = Flask(__name__)

    schema = graphene.Schema(query=Query)
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True),
    )

    return app
