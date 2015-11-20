
Installation::

  $ virtualenv-3.5 .
  $ source bin/activate

  $ pip install django
  $ pip install djangorestframework
  $ pip install djangorestframework-schemaform
  $ pip install -e ../../

Create Django Project::

  $ django-admin startproject myserver

Add djangorestframework-schemaform::

  INSTALLED_APPS = [
      ...
      'myapi'
      'rest_framework_schemaform',
  ]
