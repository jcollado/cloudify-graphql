# -*- coding: utf-8 -*-

"""Deployment module."""

import graphene


class Deployment(graphene.ObjectType):
    """A deployment."""
    blueprint_id = graphene.String(description='Blueprint ID')
    created_at = graphene.types.datetime.DateTime(
        description='Time when the deployment was created')
    created_by = graphene.String(
        description='The name of the user who created the deployment')
    description = graphene.String(description='Deployment description')
    id = graphene.String(description='Deployment ID')
    tenant_name = graphene.String(
        description='The tenant that owns the deployment')
    updated_at = graphene.types.datetime.DateTime(
        description='Time when the deployment was last updated at')
