================
Cloudify GraphQL
================


.. image:: https://img.shields.io/pypi/v/cloudify_graphql.svg
        :target: https://pypi.python.org/pypi/cloudify_graphql

.. image:: https://img.shields.io/travis/jcollado/cloudify_graphql.svg
        :target: https://travis-ci.org/jcollado/cloudify_graphql

.. image:: https://readthedocs.org/projects/cloudify-graphql/badge/?version=latest
        :target: https://cloudify-graphql.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/jcollado/cloudify_graphql/shield.svg
     :target: https://pyup.io/repos/github/jcollado/cloudify_graphql/
     :alt: Updates


Experimental Cloudify_ GraphQL_ API


* Free software: MIT license
* Documentation: https://cloudify-graphql.readthedocs.io.


Description
-----------

This project is a flask application that implements a GraphQL API that wraps
the Cloudify REST API to provide a different way to access data with the
benefits of GraphQL. As explained in GraphQL's main page:

- Ask for what you need, get exactly that
- Get many resources in a single request

Usage
-----

To give a try to this API, launch a Cloudify manager with its REST API and then
the GraphQL API as follows::

    FLASK_APP=server.py flask run

Note that for this to work the manager IP address needs to be configured in the
GraphQL API application. By default, as it can be seen in ``config.py``, this
is set to ``172.20.0.2`` which is the default IP address of the docker
container when running Cloudify through docl_.

Once the GraphQL API is running queries can be sent to it using any tool such as curl_::

    curl -X POST \
        -u admin:admin \
        -H 'Tenant: default_tenant' \
        -H 'Content-Type: application/graphql' \
        http://localhost:5000/graphql \
        -d '{ ping }'

where the ``Authorization`` and ``Tenant`` headers are passed directly to the
Cloudify REST API and are required for authentication_ purposes.

The GraphiQL_ tool is also available by opening
``http://localhost:5000/graphql`` in a web browser. Note, however, that the
browser also needs to send the ``Authorization`` and ``Tenant`` headers with
proper values, so that the GraphQL API can interact successfully with the REST
API. To do that, a browser extension such as `Modify Header Value`_ can be
used. Keep in mind that the ``Authorization`` header value can be generated
easily with something like::

    echo "Basic $(echo -n 'admin:admin' | base64)"

Query Examples
--------------

- Get all tenant names

  ::

    {
      tenants {
        name
      }
    }


- Get all blueprints and their deployments

  ::

    {
      blueprints {
        id
        deployments {
          id
        }
      }
    }


- Get all deployments and the blueprints they belong to

  ::

    {
      deployments {
        id
        blueprint {
          id
        }
      }
    }


- Get all executions and their events and logs

  ::

    {
      executions {
        logs {
          message
        }
        events {
          message
        }
      }
    }

Mutation Examples
-----------------

- Create new tenant

  ::

    mutation {
      createTenant(name: "newTenant") {
        statusCode
        tenant {
          name
        }
      }
    }

- Delete tenant

  ::

    mutation {
      deleteTenant(name: "newTenant") {
        statusCode
        tenant {
          name
        }
      }
    }

Credits
---------

This package was created with Cookiecutter_ and the
`audreyr/cookiecutter-pypackage`_ project template.

.. _Cloudify: http://cloudify.co/
.. _GraphQL: http://graphql.org/
.. _docl: https://github.com/cloudify-cosmo/docl
.. _curl: https://curl.haxx.se/
.. _authentication: http://docs.getcloudify.org/api/v3/#authentication
.. _GraphiQL: https://github.com/graphql/graphiql
.. _Modify Header Value: http://mybrowseraddon.com/modify-header-value.html

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
