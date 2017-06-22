# -*- coding: utf-8 -*-

"""Deployment module."""

from cloudify_graphql.loader import Loader


class DeploymentLoader(Loader):

    """Deployment loader."""

    ENDPOINT = 'deployments'

    @property
    def model_cls(self):
        from cloudify_graphql.model.deployment import Deployment
        return Deployment
