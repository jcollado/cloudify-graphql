# -*- coding: utf-8 -*-

"""Execution module."""

from cloudify_graphql.loader import Loader


class ExecutionLoader(Loader):

    """Execution loader."""

    ENDPOINT = 'executions'

    @property
    def model_cls(self):
        from cloudify_graphql.model.execution import Execution
        return Execution
