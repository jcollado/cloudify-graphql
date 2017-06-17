# -*- coding: utf-8 -*-

"""Blueprint module."""

import graphene


class Blueprint(graphene.ObjectType):
    """A blueprint."""
    created_at = graphene.types.datetime.DateTime(
        description='Time when the blueprint was uploaded')
    description = graphene.String(description='Blueprint description')
    id = graphene.String(description='Blueprint ID')
    main_file_name = graphene.String(description='Blueprint main file name')
    updated_at = graphene.types.datetime.DateTime(
        description='Last time when the blueprint was uploaded')
