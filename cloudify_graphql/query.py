# -*- coding: utf-8 -*-

"""GraphQL query."""

import graphene

from cloudify_graphql.model.blueprint import Blueprint
from cloudify_graphql.model.deployment import Deployment
from cloudify_graphql.model.execution import Execution
from cloudify_graphql.model.event import Event
from cloudify_graphql.model.tenant import Tenant
from cloudify_graphql.model.user import User
from cloudify_graphql.model.user_group import UserGroup

from cloudify_graphql.loader.blueprint import BlueprintLoader
from cloudify_graphql.loader.deployment import DeploymentLoader
from cloudify_graphql.loader.event import EventLoader
from cloudify_graphql.loader.execution import ExecutionLoader
from cloudify_graphql.loader.tenant import TenantLoader
from cloudify_graphql.loader.user import UserLoader
from cloudify_graphql.loader.user_group import UserGroupLoader


class Query(graphene.ObjectType):
    """Main GraphQL query."""
    blueprints = graphene.List(
        Blueprint,
        description='Cloudify blueprints',
    )
    deployments = graphene.List(
        Deployment,
        description='Cloudify deployments',
    )
    executions = graphene.List(
        Execution,
        description='Cloudify executions',
    )
    events = graphene.List(
        Event,
        description='Cloudify events',
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

    def resolve_blueprints(self, args, context, info):
        """Get list of blueprints."""
        return BlueprintLoader.get().load()

    def resolve_deployments(self, args, context, info):
        """Get list of deployments."""
        return DeploymentLoader.get().load()

    def resolve_executions(self, args, context, info):
        """Get list of executions."""
        return ExecutionLoader.get().load()

    def resolve_events(self, args, context, info):
        """Get list of executions."""
        params = {
            'type': 'cloudify_event',
        }
        return EventLoader.get().load(params)

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
