Django REST Framework Angular Schema Form
=========================================

Angular Schema Form add-on for Django Rest Framework.


Development
-----------

Setup::

  $ virtualenv-3.5 .
  $ source bin/activate
  $ pip install -r requirements/dev.txt

Run Tests::

  $ tox


Installation
------------

Install::

    $ pip install --pre djangorestframework-schemaform

Install app in Django and add content negotiation class to settings.py::

    INSTALLED_APPS = (
        ...
        'rest_framework',
        'rest_framework_schemaform',
    )

    REST_FRAMEWORK = {
        ...
        'DEFAULT_CONTENT_NEGOTIATION_CLASS':
            'rest_framework_schemaform.negotiation.IgnoreClientContentNegotiation',
   }


Content Negotiation
-------------------

http://localhost:8000/application/?format=
