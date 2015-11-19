# -*- coding: utf-8 -*-

SECRET_KEY = 'test'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
INSTALLED_APPS = (
    'rest_framework_schemaform',
)
