# -*- coding: utf-8 -*-

"""Configuration module."""


class Config(object):
    """Common configuration."""


class DevelopmentConfig(Config):
    """Development configuration."""
    MANAGER_IP = '172.20.0.2'
    TENANT = 'default_tenant'
    USER = 'admin'
    PASSWORD = 'admin'


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
}
