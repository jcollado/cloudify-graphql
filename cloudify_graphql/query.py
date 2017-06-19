# -*- coding: utf-8 -*-

"""GraphQL query."""

import graphene
import graphene.types.datetime
import requests

from flask import current_app as app

from cloudify_graphql.model.blueprint import Blueprint
from cloudify_graphql.model.deployment import Deployment
from cloudify_graphql.model.execution import Execution
from cloudify_graphql.model.tenant import Tenant
from cloudify_graphql.model.user import User
from cloudify_graphql.model.user_group import UserGroup


class Query(graphene.ObjectType):
    """Main GraphQL query."""
    blueprints = graphene.List(
        Blueprint,
        description='Cloudify blueprints',
    )
    deployments = graphene.List(
        Deployment,
        description='Cloudify deployments',
    )
    executions = graphene.List(
        Execution,
        description='Cloudify executions',
    )
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

    def resolve_blueprints(self, args, context, info):
        """Get list of blueprints."""
        url = 'http://{}/api/v3/blueprints'.format(app.config['MANAGER_IP'])
        headers = {
            'Authorization': context.headers['Authorization'],
            'Tenant': context.headers['Tenant'],
        }
        response = requests.get(
            url,
            headers=headers,
        )
        blueprints = [
            Blueprint.from_rest(blueprint_data)
            for blueprint_data
            in response.json()['items']
        ]
        return blueprints

    def resolve_deployments(self, args, context, info):
        """Get list of deployments."""
        url = 'http://{}/api/v3/deployments'.format(app.config['MANAGER_IP'])
        headers = {
            'Authorization': context.headers['Authorization'],
            'Tenant': context.headers['Tenant'],
        }
        response = requests.get(
            url,
            headers=headers,
        )
        deployments = [
            Deployment.from_rest(deployment_data)
            for deployment_data
            in response.json()['items']
        ]
        return deployments

    def resolve_executions(self, args, context, info):
        """Get list of executions."""
        url = 'http://{}/api/v3/executions'.format(app.config['MANAGER_IP'])
        headers = {
            'Authorization': context.headers['Authorization'],
            'Tenant': context.headers['Tenant'],
        }
        response = requests.get(
            url,
            headers=headers,
        )
        executions = [
            Execution.from_rest(execution_data)
            for execution_data
            in response.json()['items']
        ]
        return executions

    def resolve_ping(self, args, context, info):
        """Return ping response."""
        return 'pong'

    def resolve_tenants(self, args, context, info):
        """Get list of tenants."""
        url = 'http://{}/api/v3/tenants'.format(app.config['MANAGER_IP'])
        headers = {
            'Authorization': context.headers['Authorization'],
            'Tenant': context.headers['Tenant'],
        }
        response = requests.get(
            url,
            headers=headers,
        )
        tenants = [
            Tenant.from_rest(tenant_data)
            for tenant_data
            in response.json()['items']
        ]
        return tenants

    def resolve_users(self, args, context, info):
        """Get list of users."""
        url = 'http://{}/api/v3/users'.format(app.config['MANAGER_IP'])
        headers = {
            'Authorization': context.headers['Authorization'],
            'Tenant': context.headers['Tenant'],
        }
        response = requests.get(
            url,
            headers=headers,
        )
        users = [
            User.from_rest(user_data)
            for user_data
            in response.json()['items']
        ]
        return users

    def resolve_user_groups(self, args, context, info):
        """Get list of user groups."""
        url = 'http://{}/api/v3/user-groups'.format(app.config['MANAGER_IP'])
        headers = {
            'Authorization': context.headers['Authorization'],
            'Tenant': context.headers['Tenant'],
        }
        response = requests.get(
            url,
            headers=headers,
        )
        user_groups = [
            UserGroup.from_rest(user_group_data)
            for user_group_data
            in response.json()['items']
        ]
        return user_groups
