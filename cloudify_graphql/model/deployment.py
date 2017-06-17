# -*- coding: utf-8 -*-

"""Deployment module."""

import graphene
import iso8601
import requests

from flask import current_app as app
from requests.auth import HTTPBasicAuth

from cloudify_graphql.model.blueprint import Blueprint


class Deployment(graphene.ObjectType):
    """A deployment."""
    blueprint = graphene.Field(
        Blueprint,
        description='The blueprint the deployment is based on',
    )
    blueprint_id = graphene.String(
        description='The ID of the blueprint the deployment is based on',
    )
    created_at = graphene.types.datetime.DateTime(
        description='Time when the deployment was created')
    created_by = graphene.String(
        description='The name of the user who created the deployment')
    description = graphene.String(description='Deployment description')
    id = graphene.String(description='Deployment ID')
    tenant_name = graphene.String(
        description='The tenant that owns the deployment')
    updated_at = graphene.types.datetime.DateTime(
        description='Time when the deployment was last updated at')

    def resolve_blueprint(self, args, context, info):
        """"Get blueprint the deployment is based on."""
        url = 'http://{}/api/v3/blueprints'.format(app.config['MANAGER_IP'])
        headers = {
            'Tenant': app.config['TENANT'],
        }
        params = {
            'id': self.blueprint_id,
        }
        response = requests.get(
            url,
            auth=HTTPBasicAuth(app.config['USER'], app.config['PASSWORD']),
            headers=headers,
            params=params,
        )
        blueprint_data = response.json()['items'][0]
        blueprint = Blueprint(
            created_at=(
                iso8601.parse_date(blueprint_data['created_at'])
                if blueprint_data['created_at']
                else None
            ),
            description=blueprint_data['description'],
            id=blueprint_data['id'],
            main_file_name=blueprint_data['main_file_name'],
            updated_at=(
                iso8601.parse_date(blueprint_data['updated_at'])
                if blueprint_data['updated_at']
                else None
            ),
        )
        return blueprint
