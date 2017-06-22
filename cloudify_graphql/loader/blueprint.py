# -*- coding: utf-8 -*-

"""Blueprint module."""

from cloudify_graphql.loader import Loader


class BlueprintLoader(Loader):

    """Blueprint loader."""

    ENDPOINT = 'blueprints'

    @property
    def model_cls(self):
        from cloudify_graphql.model.blueprint import Blueprint
        return Blueprint
