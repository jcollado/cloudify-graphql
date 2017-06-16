# -*- coding: utf-8 -*-

"""GraphQL query."""

import graphene
import requests

from flask import current_app as app
from requests.auth import HTTPBasicAuth


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
        url = 'http://{}/api/v3/tenants'.format(app.config['MANAGER_IP'])
        headers = {
            'Tenant': app.config['TENANT'],
        }
        response = requests.get(
            url,
            auth=HTTPBasicAuth(app.config['USER'], app.config['PASSWORD']),
            headers=headers,
        )
        tenants = [
            Tenant(**tenant_data)
            for tenant_data
            in response.json()['items']
        ]
        return tenants
