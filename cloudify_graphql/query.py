# -*- coding: utf-8 -*-

"""GraphQL query."""

import graphene
import graphene.types.datetime
import iso8601
import requests

from flask import current_app as app
from requests.auth import HTTPBasicAuth


class Tenant(graphene.ObjectType):
    """A tenant."""
    groups = graphene.Int(description='Group count')
    name = graphene.String(description='Tenant name')
    users = graphene.Int(description='User count')


class User(graphene.ObjectType):
    """A user."""
    active = graphene.Boolean(description='User status (active or suspended)')
    groups = graphene.Int(description='Group count')
    last_login_at = graphene.types.datetime.DateTime(
        description='Date of last request performed by the user')
    role = graphene.String(description='User role (admin or user)')
    tenants = graphene.Int(description='Tenant count')
    username = graphene.String(description='User name')


class Query(graphene.ObjectType):
    """Main GraphQL query."""
    ping = graphene.String(description='Check API status')
    tenants = graphene.List(
        Tenant,
        description='Cloudify tenants',
    )
    users = graphene.List(
        User,
        description='Cloudify users',
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

    def resolve_users(self, args, context, info):
        """Get list of users."""
        url = 'http://{}/api/v3/users'.format(app.config['MANAGER_IP'])
        headers = {
            'Tenant': app.config['TENANT'],
        }
        response = requests.get(
            url,
            auth=HTTPBasicAuth(app.config['USER'], app.config['PASSWORD']),
            headers=headers,
        )
        users = [
            User(
                active=user_data['active'],
                groups=user_data['groups'],
                last_login_at=(
                    iso8601.parse_date(user_data['last_login_at'])
                    if user_data['last_login_at']
                    else None
                ),
                role=user_data['role'],
                tenants=user_data['tenants'],
                username=user_data['username'],
            )
            for user_data
            in response.json()['items']
        ]
        return users
