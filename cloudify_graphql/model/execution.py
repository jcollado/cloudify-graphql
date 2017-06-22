# -*- coding: utf-8 -*-

"""Execution module."""

import graphene
import graphene.types.datetime
import iso8601

from cloudify_graphql.loader.blueprint import BlueprintLoader
from cloudify_graphql.loader.deployment import DeploymentLoader


class Execution(graphene.ObjectType):
    """An execution."""
    blueprint = graphene.Field(
        'cloudify_graphql.model.blueprint.Blueprint',
        description='The blueprint the execution is in the context of',
    )
    blueprint_id = graphene.String(
        description=(
            'The ID of the blueprint the execution is in the context of'
        )
    )
    created_at = graphene.types.datetime.DateTime(
        description='Time when the execution was queued at')
    created_by = graphene.String(
        description='The name of the user who created the exeuction')
    deployment = graphene.Field(
        'cloudify_graphql.model.deployment.Deployment',
        description='The deployment the execution is in the context of',
    )
    deployment_id = graphene.String(
        description=(
            'The ID of the deployment the execution is in the context of'
        )
    )
    error = graphene.String(
        description='The execution error message on failure'
    )
    id = graphene.String(description='Execution ID')
    is_system_workflow = graphene.Boolean(
        description='Whether the execution is a system workflow or not'
    )
    status = graphene.String(description='Execution status')
    tenant_name = graphene.String(
        description='The tenant that owns the execution')
    workflow_id = graphene.String(
        description='The id/name of the workflow the execution is of'
    )

    @classmethod
    def from_rest(cls, execution_data):
        """Create execution from REST data."""
        return cls(
            blueprint_id=execution_data['blueprint_id'],
            created_at=(
                iso8601.parse_date(execution_data['created_at'])
                if execution_data['created_at']
                else None
            ),
            created_by=execution_data['created_by'],
            deployment_id=execution_data['deployment_id'],
            error=execution_data['error'],
            id=execution_data['id'],
            is_system_workflow=execution_data['is_system_workflow'],
            status=execution_data['status'],
            tenant_name=execution_data['tenant_name'],
            workflow_id=execution_data['workflow_id'],
        )

    def resolve_blueprint(self, args, context, info):
        """"Get blueprint the execution is in the context of."""
        params = {
            'id': self.blueprint_id,
        }
        return BlueprintLoader.get().load(params)[0]

    def resolve_deployment(self, args, context, info):
        """"Get deployment the execution is in the context of."""
        params = {
            'id': self.deployment_id,
        }
        return DeploymentLoader.get().load(params)[0]