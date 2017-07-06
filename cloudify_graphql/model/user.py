# -*- coding: utf-8 -*-

"""User module."""

import graphene
import graphene.types.datetime
import iso8601


class Role(graphene.Enum):
    """User role."""
    USER = 'user'
    ADMIN = 'admin'
    SUSPENDED = 'suspended'


class User(graphene.ObjectType):
    """A user."""
    active = graphene.Boolean(description='User status (active or suspended)')
    groups = graphene.Int(description='Group count')
    last_login_at = graphene.types.datetime.DateTime(
        description='Date of last request performed by the user')
    role = graphene.Field(Role, description='User role')
    tenants = graphene.Int(description='Tenant count')
    username = graphene.String(description='User name')

    @classmethod
    def from_rest(cls, user_data):
        """Create user from REST data."""
        return cls(
            active=user_data['active'],
            groups=user_data['groups'],
            last_login_at=(
                iso8601.parse_date(user_data['last_login_at'])
                if user_data['last_login_at']
                else None
            ),
            role=user_data['role'],
            tenants=user_data['tenants'],
            username=user_data['username'],
        )
