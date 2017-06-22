# -*- coding: utf-8 -*-

"""Event module."""

from cloudify_graphql.loader import Loader


class EventLoader(Loader):

    """Event loader."""

    ENDPOINT = 'events'

    DEFAULT_PARAMS = {
        'type': 'cloudify_event'
    }

    @property
    def model_cls(self):
        from cloudify_graphql.model.event import Event
        return Event
