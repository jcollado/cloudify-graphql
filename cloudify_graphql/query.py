# -*- coding: utf-8 -*-

"""GraphQL query."""

import graphene
import graphene.types.datetime
import iso8601
import requests

from flask import current_app as app
from requests.auth import HTTPBasicAuth

from cloudify_graphql.model.tenant import Tenant
from cloudify_graphql.model.user import User
from cloudify_graphql.model.user_group import UserGroup


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
    user_groups = graphene.List(
        UserGroup,
        description='Cloudify user groups',
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

    def resolve_user_groups(self, args, context, info):
        """Get list of user groups."""
        url = 'http://{}/api/v3/user-groups'.format(app.config['MANAGER_IP'])
        headers = {
            'Tenant': app.config['TENANT'],
        }
        response = requests.get(
            url,
            auth=HTTPBasicAuth(app.config['USER'], app.config['PASSWORD']),
            headers=headers,
        )
        user_groups = [
            UserGroup(
                name=user_group_data['name'],
                tenants=user_group_data['tenants'],
                users=user_group_data['users'],
            )
            for user_group_data
            in response.json()['items']
        ]
        return user_groups