# -*- coding: utf-8 -*-

"""GraphQL query."""

import graphene

from cloudify_graphql.model.blueprint import Blueprint
from cloudify_graphql.model.deployment import Deployment
from cloudify_graphql.model.event import Event
from cloudify_graphql.model.execution import Execution
from cloudify_graphql.model.log import Log
from cloudify_graphql.model.tenant import Tenant
from cloudify_graphql.model.user import User
from cloudify_graphql.model.user_group import UserGroup

from cloudify_graphql.loader.blueprint import BlueprintLoader
from cloudify_graphql.loader.deployment import DeploymentLoader
from cloudify_graphql.loader.event import EventLoader
from cloudify_graphql.loader.execution import ExecutionLoader
from cloudify_graphql.loader.log import LogLoader
from cloudify_graphql.loader.tenant import TenantLoader
from cloudify_graphql.loader.user import UserLoader
from cloudify_graphql.loader.user_group import UserGroupLoader


class Query(graphene.ObjectType):
    """Main GraphQL query."""
    blueprint = graphene.Field(
        Blueprint,
        id=graphene.Argument(
            graphene.ID,
            required=True,
            description='Blueprint ID',
        ),
        description='Cloudify blueprint',
    )
    blueprints = graphene.List(
        Blueprint,
        description='Cloudify blueprints',
    )
    deployment = graphene.Field(
        Deployment,
        id=graphene.Argument(
            graphene.ID,
            required=True,
            description='Deployment ID',
        ),
        description='Cloudify deployment',
    )
    deployments = graphene.List(
        Deployment,
        description='Cloudify deployments',
    )
    execution = graphene.Field(
        Execution,
        id=graphene.Argument(
            graphene.ID,
            required=True,
            description='Execution ID',
        ),
        description='Cloudify execution',
    )
    executions = graphene.List(
        Execution,
        description='Cloudify executions',
    )
    events = graphene.List(
        Event,
        description='Cloudify events',
    )
    logs = graphene.List(
        Log,
        description='Cloudify logs',
    )
    ping = graphene.String(description='Check API status')
    tenants = graphene.List(
        Tenant,
        description='Cloudify tenants',
    )
    users = graphene.List(
        User,
        description='Cloudify users',
    )
    user_groups = graphene.List(
        UserGroup,
        description='Cloudify user groups',
    )

    def resolve_blueprint(self, args, context, info):
        """Get blueprint by ID."""
        blueprints = BlueprintLoader.get().load(args)
        return blueprints[0] if blueprints else None

    def resolve_blueprints(self, args, context, info):
        """Get list of blueprints."""
        return BlueprintLoader.get().load()

    def resolve_deployment(self, args, context, info):
        """Get deployment by ID."""
        deployments = DeploymentLoader.get().load(args)
        return deployments[0] if deployments else None

    def resolve_deployments(self, args, context, info):
        """Get list of deployments."""
        return DeploymentLoader.get().load()

    def resolve_execution(self, args, context, info):
        """Get execution by ID."""
        executions = ExecutionLoader.get().load(args)
        return executions[0] if executions else None

    def resolve_executions(self, args, context, info):
        """Get list of executions."""
        return ExecutionLoader.get().load()

    def resolve_events(self, args, context, info):
        """Get list of executions."""
        return EventLoader.get().load()

    def resolve_logs(self, args, context, info):
        """Get list of executions."""
        return LogLoader.get().load()

    def resolve_ping(self, args, context, info):
        """Return ping response."""
        return 'pong'

    def resolve_tenants(self, args, context, info):
        """Get list of tenants."""
        return TenantLoader.get().load()

    def resolve_users(self, args, context, info):
        """Get list of users."""
        return UserLoader.get().load()

    def resolve_user_groups(self, args, context, info):
        """Get list of user groups."""
        return UserGroupLoader.get().load()
