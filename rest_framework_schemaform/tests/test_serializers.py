# -*- coding: utf-8 -*-
from rest_framework_schemaform.serializers import JsonSchemaSerializer
from rest_framework_schemaform.models import Application

import pytest


@pytest.mark.django_db
def test_char_field_serializer():
    from rest_framework_schemaform.models import CharFieldModel

    model = CharFieldModel()
    model.field = u'My CharFieldTest'
    model.save()

    serializer = JsonSchemaSerializer(model)
    result = serializer.to_representation(model)

    assert 'field' == result.get('properties').get('field').get('key')
    assert 'Field Title' == result.get('properties').get('field').get('title')
    assert 'Field Help Text' == result.get('properties').get('field').get('description')  # noqa
    assert 'string' == result.get('properties').get('field').get('type')
    assert 'integer' == result.get('properties').get('id').get('type')


@pytest.mark.django_db
def test_foreign_key_field_serializer():
    from rest_framework_schemaform.models import CharFieldModel
    from rest_framework_schemaform.models import ForeignKeyModel

    reference = CharFieldModel()
    reference.field = u'My CharFieldTest'
    reference.save()

    model = ForeignKeyModel()
    model.field = reference
    model.save()

    serializer = JsonSchemaSerializer(model)
    result = serializer.to_representation(model)


@pytest.mark.django_db
def test_json_schema_serializer():
    app = Application()
    app.title = u'My first application'
    app.firstname = u'John'
    app.lastname = u'Doe'
    app.email = u'john@doe.com'
    app.save()

    serializer = JsonSchemaSerializer(app)
    result = serializer.to_representation(app)

    assert result.get('title').startswith('Application')
    assert 'object' == result.get('type')

    assert 'salutation' == result['properties']['salutation']['key']
    assert 'salutation' == result['properties']['salutation']['title']
    assert 'string' == result['properties']['salutation']['type']
    assert 'salutation' in result['form']

    assert 'firstname' == result['properties']['firstname']['key']
    assert 'First name' == result['properties']['firstname']['title']
    assert 'string' == result['properties']['firstname']['type']
    assert 'firstname' in result['required']
    assert 'firstname' in result['form']

    assert 'lastname' == result['properties']['lastname']['key']
    assert 'Last name' == result['properties']['lastname']['title']
    assert 'string' == result['properties']['lastname']['type']
    assert 'lastname' in result['form']

    assert 'email' == result['properties']['email']['key']
    assert 'Email address' == result['properties']['email']['title']
    assert 'string' == result['properties']['email']['type']
    assert '^\\S+@\\S+$' == result['properties']['email']['pattern']
    assert 'email' in result['form']

    assert 'first_time_application' == result['properties']['first_time_application']['key']  # noqa
    assert 'first_time_application' == result['properties']['first_time_application']['title']  # noqa
    assert 'boolean' == result['properties']['first_time_application']['type']
    assert 'first_time_application' in result['form']
