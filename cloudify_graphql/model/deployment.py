# -*- coding: utf-8 -*-

"""Deployment module."""

import graphene
import graphene.types.datetime
import iso8601

from cloudify_graphql.loader.blueprint import BlueprintLoader
from cloudify_graphql.loader.execution import ExecutionLoader
from cloudify_graphql.loader.event import EventLoader
from cloudify_graphql.loader.log import LogLoader


class Deployment(graphene.ObjectType):
    """A deployment."""
    blueprint = graphene.Field(
        'cloudify_graphql.model.blueprint.Blueprint',
        description='The blueprint the deployment is based on',
    )
    blueprint_id = graphene.ID(
        description='The ID of the blueprint the deployment is based on',
    )
    created_at = graphene.types.datetime.DateTime(
        description='Time when the deployment was created')
    created_by = graphene.String(
        description='The name of the user who created the deployment')
    description = graphene.String(description='Deployment description')
    executions = graphene.List(
        'cloudify_graphql.model.execution.Execution',
        description='The executions based on the deployment.'
    )
    events = graphene.List(
        'cloudify_graphql.model.event.Event',
        description='The events based on the deployment.'
    )
    id = graphene.ID(description='Deployment ID')
    logs = graphene.List(
        'cloudify_graphql.model.log.Log',
        description='The logs based on the deployment.'
    )
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
        params = {
            'id': self.blueprint_id,
        }
        return BlueprintLoader.get().load(params)[0]

    def resolve_executions(self, args, context, info):
        """Get executions based on the blueprint."""
        params = {
            'deployment_id': self.id,
        }
        return ExecutionLoader.get().load(params)

    def resolve_events(self, args, context, info):
        """Get events based on the blueprint."""
        params = {
            'deployment_id': self.id,
        }
        return EventLoader.get().load(params)

    def resolve_logs(self, args, context, info):
        """Get logs based on the deployment."""
        params = {
            'deployment_id': self.id,
        }
        return LogLoader.get().load(params)
