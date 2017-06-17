# -*- coding: utf-8 -*-

"""User group module."""

import graphene


class UserGroup(graphene.ObjectType):
    """A user group."""
    name = graphene.String(description='Name')
    tenants = graphene.Int(description='Tenant count')
    users = graphene.Int(description='User count')

    @classmethod
    def from_rest(cls, user_group_data):
        """Create user group from REST data."""
        return cls(
            name=user_group_data['name'],
            tenants=user_group_data['tenants'],
            users=user_group_data['users'],
        )
