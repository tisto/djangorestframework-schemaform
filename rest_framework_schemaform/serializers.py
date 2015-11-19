# -*- coding: utf-8 -*-
from rest_framework import serializers
from collections import OrderedDict
from rest_framework_schemaform.mapping import REST_MODEL_TO_JSON_SCHEMA_MAPPING


class JsonSchemaSerializer(serializers.ModelSerializer):

    class Meta:
        model = None

    def __init__(self, instance):
        self.Meta.model = type(instance)
        super(JsonSchemaSerializer, self).__init__(instance=instance)

    def get_fields(self, *args, **kwargs):
        fields = super(JsonSchemaSerializer, self).get_fields(*args, **kwargs)
        return fields

    def to_representation(self, obj):
        result = {
            'title': self.Meta.model.__doc__,
            'type': 'object',
            'form': [],
            'required': [],
            'properties': OrderedDict()
        }
        # Schema
        for key, value in self.get_fields().items():
            mapping_dict = REST_MODEL_TO_JSON_SCHEMA_MAPPING[type(value)]
            result['properties'][key] = {
                'key': key,
                'title': value.label or key,
                'description': value.help_text or '',
            }
            for m_key, m_value in mapping_dict.items():
                result['properties'][key][m_key] = m_value

        # Required
        for key, value in self.get_fields().items():
            if value.required:
                result['required'].append(key)
        # Form Helper
        result['form'].append({
            'type': 'help',
            'helpvalue': '<div class="alert alert-info">Example Form</div>'
        })

        # Form Keys
        for key, value in self.get_fields().items():
            result['form'].append(key)

        # Form Actions
        result['form'].append(
            {
                'type': 'submit',
                'title': 'Save'
            }
        )
        result['form'].append(
            {
                'type': 'button',
                'title': 'Cancel',
                'style': 'btn-default',
                'onClick': 'clearForm(form)'
            }
        )
        return result
