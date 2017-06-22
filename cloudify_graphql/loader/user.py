# -*- coding: utf-8 -*-

"""User module."""

from cloudify_graphql.loader import Loader


class UserLoader(Loader):

    """User loader."""

    ENDPOINT = 'users'

    @property
    def model_cls(self):
        from cloudify_graphql.model.user import User
        return User
