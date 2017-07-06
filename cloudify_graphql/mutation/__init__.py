# -*- coding: utf-8 -*-

"""GraphQL mutation."""

import graphene

from cloudify_graphql.mutation.tenant import (
    CreateTenant,
    DeleteTenant,
)
from cloudify_graphql.mutation.user import (
    CreateUser,
    DeleteUser,
)


class Mutation(graphene.ObjectType):
    """Main GraphQL mutation."""
    create_tenant = CreateTenant.Field(description='Create Cloudify tenant')
    delete_tenant = DeleteTenant.Field(description='Delete Cloudify tenant')

    create_user = CreateUser.Field(description='Create Cloudify user')
    delete_user = DeleteUser.Field(description='Delete Cloudify user')
