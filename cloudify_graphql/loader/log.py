# -*- coding: utf-8 -*-

"""Log module."""

from cloudify_graphql.loader import Loader


class LogLoader(Loader):

    """Log loader."""

    ENDPOINT = 'events'

    DEFAULT_PARAMS = {
        'type': 'cloudify_log'
    }

    @property
    def model_cls(self):
        from cloudify_graphql.model.log import Log
        return Log
