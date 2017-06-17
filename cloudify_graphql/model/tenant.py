# -*- coding: utf-8 -*-

"""Tenant module."""

import graphene


class Tenant(graphene.ObjectType):
    """A tenant."""
    groups = graphene.Int(description='Group count')
    name = graphene.String(description='Tenant name')
    users = graphene.Int(description='User count')
