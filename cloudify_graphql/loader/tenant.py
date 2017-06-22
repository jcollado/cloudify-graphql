# -*- coding: utf-8 -*-

"""Tenant module."""

from cloudify_graphql.loader import Loader


class TenantLoader(Loader):

    """Tenant loader."""

    ENDPOINT = 'tenants'

    @property
    def model_cls(self):
        from cloudify_graphql.model.tenant import Tenant
        return Tenant
