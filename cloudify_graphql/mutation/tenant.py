# -*- coding: utf-8 -*-

"""Tenant mutations."""

import graphene
import requests

from flask import (
    current_app as app,
    request,
)

from cloudify_graphql.model.tenant import Tenant


class CreateTenant(graphene.Mutation):

    """Create tenant mutation."""

    class Input(object):
        name = graphene.String(description='Tenant name', required=True)

    error_code = graphene.String(description='Response error code')
    message = graphene.String(description='Response message')
    status_code = graphene.Int(description='Response status code')
    tenant = graphene.Field(Tenant, description='Created tenant')

    def mutate(self, args, context, info):
        """Create new tenant with the given name."""
        url = (
            'http://{}/api/v3/tenants/{}'
            .format(app.config['MANAGER_IP'], args['name'])
        )
        headers = {
            'Authorization': request.headers['Authorization'],
            'Tenant': request.headers['Tenant'],
        }
        response = requests.post(
            url,
            headers=headers,
        )
        response_json = response.json()
        tenant = None
        if response.status_code == 201:
            tenant = Tenant.from_rest(response_json)
        return CreateTenant(
            error_code=response_json.get('error_code'),
            message=response_json.get('message'),
            status_code=response.status_code,
            tenant=tenant,
        )


class DeleteTenant(graphene.Mutation):

    """Delete tenant mutation."""

    class Input(object):
        name = graphene.String(description='Tenant name', required=True)

    error_code = graphene.String(description='Response error code')
    message = graphene.String(description='Response message')
    status_code = graphene.Int(description='Response status code')
    tenant = graphene.Field(Tenant, description='Deleted tenant')

    def mutate(self, args, context, info):
        """Delete tenant by name."""
        url = (
            'http://{}/api/v3/tenants/{}'
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
        tenant = None
        if response.status_code == 200:
            tenant = Tenant.from_rest(response_json)
        return DeleteTenant(
            error_code=response_json.get('error_code'),
            message=response_json.get('message'),
            status_code=response.status_code,
            tenant=tenant,
        )
