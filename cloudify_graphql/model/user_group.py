# -*- coding: utf-8 -*-

"""User group module."""

import graphene


class UserGroup(graphene.ObjectType):
    """A user group."""
    name = graphene.String(description='Name')
    tenants = graphene.Int(description='Tenant count')
    users = graphene.Int(description='User count')
