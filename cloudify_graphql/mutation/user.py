# -*- coding: utf-8 -*-

"""User mutations."""

import graphene
import requests

from flask import (
    current_app as app,
    request,
)

from cloudify_graphql.model.user import (
    Role,
    User,
)


class CreateUser(graphene.Mutation):

    """Create user mutation."""

    class Input(object):
        name = graphene.String(description='User name', required=True)
        password = graphene.String(description='User password', required=True)
        role = graphene.Argument(
            Role,
            description='User role (USER by default)',
            default_value='user',
        )

    error_code = graphene.String(description='Response error code')
    message = graphene.String(description='Response message')
    status_code = graphene.Int(description='Response status code')
    user = graphene.Field(User, description='New user')

    def mutate(self, args, context, info):
        """Create new user with the given name."""
        url = (
            'http://{}/api/v3/users'
            .format(app.config['MANAGER_IP'])
        )
        headers = {
            'Authorization': request.headers['Authorization'],
            'Tenant': request.headers['Tenant'],
        }
        data = {
            'username': args['name'],
            'password': args['password'],
            'role': args['role'],
        }
        response = requests.put(
            url,
            headers=headers,
            json=data,
        )
        response_json = response.json()
        user = None
        if response.status_code == 201:
            user = User.from_rest(response_json)
        return CreateUser(
            error_code=response_json.get('error_code'),
            message=response_json.get('message'),
            status_code=response.status_code,
            user=user,
        )


class DeleteUser(graphene.Mutation):

    """Delete user mutation."""

    class Input(object):
        name = graphene.String(description='User name', required=True)

    error_code = graphene.String(description='Response error code')
    message = graphene.String(description='Response message')
    status_code = graphene.Int(description='Response status code')
    user = graphene.Field(User, description='Deleted user')

    def mutate(self, args, context, info):
        """Delete user by name."""
        url = (
            'http://{}/api/v3/users/{}'
            .format(app.config['MANAGER_IP'], args['name'])
        )
        headers = {
            'Authorization': request.headers['Authorization'],
            'Tenant': request.headers['Tenant'],
        }
        response = requests.delete(
            url,
            headers=headers,
        )
        response_json = response.json()
        user = None
        if response.status_code == 200:
            user = User.from_rest(response_json)
        return DeleteUser(
            error_code=response_json.get('error_code'),
            message=response_json.get('message'),
            status_code=response.status_code,
            user=user,
        )
