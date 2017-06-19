# -*- coding: utf-8 -*-

"""Blueprint module."""

import graphene
import iso8601
import requests

from flask import current_app as app


class Blueprint(graphene.ObjectType):
    """A blueprint."""
    created_at = graphene.types.datetime.DateTime(
        description='Time when the blueprint was uploaded')
    deployments = graphene.List(
        'cloudify_graphql.model.deployment.Deployment',
        description='The deployments based on the blueprint.'
    )
    description = graphene.String(description='Blueprint description')
    id = graphene.String(description='Blueprint ID')
    main_file_name = graphene.String(description='Blueprint main file name')
    updated_at = graphene.types.datetime.DateTime(
        description='Last time when the blueprint was uploaded')

    @classmethod
    def from_rest(cls, blueprint_data):
        """Create blueprint from REST data."""
        return cls(
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

    def resolve_deployments(self, args, context, info):
        """Get deployments based on the blueprint."""
        from cloudify_graphql.model.deployment import Deployment

        url = 'http://{}/api/v3/deployments'.format(app.config['MANAGER_IP'])
        headers = {
            'Authorization': context.headers['Authorization'],
            'Tenant': context.headers['Tenant'],
        }
        params = {
            'blueprint_id': self.id,
        }
        response = requests.get(
            url,
            headers=headers,
            params=params,
        )
        deployments = [
            Deployment.from_rest(deployment_data)
            for deployment_data
            in response.json()['items']
        ]
        return deployments
