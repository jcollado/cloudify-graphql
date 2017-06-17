# -*- coding: utf-8 -*-

"""Deployment module."""

import graphene
import iso8601
import requests

from flask import current_app as app
from requests.auth import HTTPBasicAuth


class Deployment(graphene.ObjectType):
    """A deployment."""
    blueprint = graphene.Field(
        'cloudify_graphql.model.blueprint.Blueprint',
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

    @classmethod
    def from_rest(cls, deployment_data):
        """Create deployment from REST data."""
        return cls(
            blueprint_id=deployment_data['blueprint_id'],
            created_at=(
                iso8601.parse_date(deployment_data['created_at'])
                if deployment_data['created_at']
                else None
            ),
            created_by=deployment_data['created_by'],
            description=deployment_data['description'],
            id=deployment_data['id'],
            tenant_name=deployment_data['tenant_name'],
            updated_at=(
                iso8601.parse_date(deployment_data['updated_at'])
                if deployment_data['updated_at']
                else None
            ),
        )

    def resolve_blueprint(self, args, context, info):
        """"Get blueprint the deployment is based on."""
        from cloudify_graphql.model.blueprint import Blueprint

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
        blueprint = Blueprint.from_rest(blueprint_data)
        return blueprint
