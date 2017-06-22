# -*- coding: utf-8 -*-

"""Event module."""

import graphene
import graphene.types.datetime
import iso8601

from cloudify_graphql.loader.blueprint import BlueprintLoader
from cloudify_graphql.loader.deployment import DeploymentLoader


class Event(graphene.ObjectType):
    """An event."""
    blueprint = graphene.Field(
        'cloudify_graphql.model.blueprint.Blueprint',
        description='The blueprint the event is in the context of',
    )
    blueprint_id = graphene.String(
        description='The ID of the blueprint the event is in the context of'
    )
    deployment = graphene.Field(
        'cloudify_graphql.model.deployment.Deployment',
        description='The deployment the event is in the context of',
    )
    deployment_id = graphene.String(
        description='The ID of the deployment the event is in the context of'
    )
    event_type = graphene.String(description='Event type name')
    execution_id = graphene.String(
        description='The ID of the running execution when the event happened'
    )
    message = graphene.String(description='Message text')
    node_instance_id = graphene.String(
        description='The ID of the node instance that reported the event'
    )
    node_name = graphene.String(
        description='Name of the node that reported the event'
    )
    operation = graphene.String(description='Operation name')
    reported_timestamp = graphene.types.datetime.DateTime(
        description='Time at which the event occurred on the executing machine'
    )
    timestamp = graphene.types.datetime.DateTime(
        description=(
            'Time at which the event was logged on the management machine'
        )
    )
    type = graphene.String(
        description='Underlying REST resource type (cloudify-event)'
    )
    workflow_id = graphene.String(
        description='The ID of the executing workflow when the event happened'
    )

    @classmethod
    def from_rest(cls, event_data):
        """Create event from REST data."""
        return cls(
            blueprint_id=event_data['blueprint_id'],
            deployment_id=event_data['deployment_id'],
            event_type=event_data['event_type'],
            execution_id=event_data['execution_id'],
            message=event_data['message'],
            node_instance_id=event_data['node_instance_id'],
            node_name=event_data['node_name'],
            operation=event_data['operation'],
            reported_timestamp=(
                iso8601.parse_date(event_data['reported_timestamp'])
                if event_data['reported_timestamp']
                else None
            ),
            timestamp=(
                iso8601.parse_date(event_data['timestamp'])
                if event_data['timestamp']
                else None
            ),
            type=event_data['type'],
            workflow_id=event_data['workflow_id'],
        )

    def resolve_blueprint(self, args, context, info):
        """"Get blueprint the event is in the context of."""
        params = {
            'id': self.blueprint_id,
        }
        return BlueprintLoader.get().load(params)[0]

    def resolve_deployment(self, args, context, info):
        """"Get deployment the event is in the context of."""
        params = {
            'id': self.deployment_id,
        }
        return DeploymentLoader.get().load(params)[0]
