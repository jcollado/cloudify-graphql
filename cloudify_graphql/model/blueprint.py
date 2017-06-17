# -*- coding: utf-8 -*-

"""Blueprint module."""

import graphene
import iso8601


class Blueprint(graphene.ObjectType):
    """A blueprint."""
    created_at = graphene.types.datetime.DateTime(
        description='Time when the blueprint was uploaded')
    description = graphene.String(description='Blueprint description')
    id = graphene.String(description='Blueprint ID')
    main_file_name = graphene.String(description='Blueprint main file name')
    updated_at = graphene.types.datetime.DateTime(
        description='Last time when the blueprint was uploaded')

    @classmethod
    def from_rest(cls, blueprint_data):
        """Create blueprint from REST data."""
        return cls(
            created_at=(
                iso8601.parse_date(blueprint_data['created_at'])
                if blueprint_data['created_at']
                else None
            ),
            description=blueprint_data['description'],
            id=blueprint_data['id'],
            main_file_name=blueprint_data['main_file_name'],
            updated_at=(
                iso8601.parse_date(blueprint_data['updated_at'])
                if blueprint_data['updated_at']
                else None
            ),
        )
