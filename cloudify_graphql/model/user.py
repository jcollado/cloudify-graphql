# -*- coding: utf-8 -*-

"""User module."""

import graphene


class User(graphene.ObjectType):
    """A user."""
    active = graphene.Boolean(description='User status (active or suspended)')
    groups = graphene.Int(description='Group count')
    last_login_at = graphene.types.datetime.DateTime(
        description='Date of last request performed by the user')
    role = graphene.String(description='User role (admin or user)')
    tenants = graphene.Int(description='Tenant count')
    username = graphene.String(description='User name')
