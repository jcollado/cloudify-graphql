# -*- coding: utf-8 -*-

"""Log module."""

import graphene
import graphene.types.datetime
import iso8601

from cloudify_graphql.loader.blueprint import BlueprintLoader
from cloudify_graphql.loader.deployment import DeploymentLoader
from cloudify_graphql.loader.execution import ExecutionLoader


class Log(graphene.ObjectType):
    """A log."""
    blueprint = graphene.Field(
        'cloudify_graphql.model.blueprint.Blueprint',
        description='The blueprint the log is in the context of',
    )
    blueprint_id = graphene.String(
        description='The ID of the blueprint the log is in the context of'
    )
    deployment = graphene.Field(
        'cloudify_graphql.model.deployment.Deployment',
        description='The deployment the log is in the context of',
    )
    deployment_id = graphene.String(
        description='The ID of the deployment the log is in the context of'
    )
    execution = graphene.Field(
        'cloudify_graphql.model.execution.Execution',
        description='The running execution when the log happened',
    )
    execution_id = graphene.String(
        description='The ID of the running execution when the log happened'
    )
    level = graphene.String(description='Log level')
    logger = graphene.String(description='Logger ID')
    message = graphene.String(description='Message text')
    node_instance_id = graphene.String(
        description='The ID of the node instance that reported the log'
    )
    node_name = graphene.String(
        description='Name of the node that reported the log'
    )
    operation = graphene.String(description='Operation name')
    reported_timestamp = graphene.types.datetime.DateTime(
        description='Time at which the log occurred on the executing machine'
    )
    timestamp = graphene.types.datetime.DateTime(
        description=(
            'Time at which the message was logged on the management machine'
        )
    )
    type = graphene.String(
        description='Underlying REST resource type (cloudify-log)'
    )
    workflow_id = graphene.String(
        description=(
            'The ID of the executing workflow when the message was logged'
        )
    )

    @classmethod
    def from_rest(cls, log_data):
        """Create log from REST data."""
        return cls(
            blueprint_id=log_data['blueprint_id'],
            deployment_id=log_data['deployment_id'],
            execution_id=log_data['execution_id'],
            level=log_data['level'],
            logger=log_data['logger'],
            message=log_data['message'],
            node_instance_id=log_data['node_instance_id'],
            node_name=log_data['node_name'],
            operation=log_data['operation'],
            reported_timestamp=(
                iso8601.parse_date(log_data['reported_timestamp'])
                if log_data['reported_timestamp']
                else None
            ),
            timestamp=(
                iso8601.parse_date(log_data['timestamp'])
                if log_data['timestamp']
                else None
            ),
            type=log_data['type'],
            workflow_id=log_data['workflow_id'],
        )

    def resolve_blueprint(self, args, context, info):
        """"Get blueprint the log is in the context of."""
        params = {
            'id': self.blueprint_id,
        }
        return BlueprintLoader.get().load(params)[0]

    def resolve_deployment(self, args, context, info):
        """"Get deployment the log is in the context of."""
        params = {
            'id': self.deployment_id,
        }
        return DeploymentLoader.get().load(params)[0]

    def resolve_execution(self, args, context, info):
        """Get the running execution when the log happened."""
        params = {
            'id': self.execution_id
        }
        return ExecutionLoader.get().load(params)[0]
