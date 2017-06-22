# -*- coding: utf-8 -*-

"""Blueprint module."""

import graphene
import graphene.types.datetime
import iso8601

from cloudify_graphql.loader.deployment import DeploymentLoader
from cloudify_graphql.loader.execution import ExecutionLoader
from cloudify_graphql.loader.event import EventLoader


class Blueprint(graphene.ObjectType):
    """A blueprint."""
    created_at = graphene.types.datetime.DateTime(
        description='Time when the blueprint was uploaded')
    deployments = graphene.List(
        'cloudify_graphql.model.deployment.Deployment',
        description='The deployments based on the blueprint.'
    )
    executions = graphene.List(
        'cloudify_graphql.model.execution.Execution',
        description='The executions based on the blueprint.'
    )
    events = graphene.List(
        'cloudify_graphql.model.event.Event',
        description='The events based on the blueprint.'
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
        params = {
            'blueprint_id': self.id,
        }
        return DeploymentLoader.get().load(params)

    def resolve_executions(self, args, context, info):
        """Get executions based on the blueprint."""
        params = {
            'blueprint_id': self.id,
        }
        return ExecutionLoader.get().load(params)

    def resolve_events(self, args, context, info):
        """Get events based on the blueprint."""
        params = {
            'blueprint_id': self.id,
            'type': 'cloudify_event',
        }
        return EventLoader.get().load(params)
