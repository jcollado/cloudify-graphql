# -*- coding: utf-8 -*-

"""User group module."""

from cloudify_graphql.loader import Loader


class UserGroupLoader(Loader):

    """User group loader."""

    ENDPOINT = 'user-groups'

    @property
    def model_cls(self):
        from cloudify_graphql.model.user_group import UserGroup
        return UserGroup
