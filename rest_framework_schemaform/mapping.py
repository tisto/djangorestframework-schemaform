# -*- coding: utf-8 -*-
from rest_framework import fields

# Mapping from Django REST Framework models to JSON schema
# http://www.django-rest-framework.org/api-guide/fields/
# http://json-schema.org/latest/json-schema-core.html#anchor8
REST_MODEL_TO_JSON_SCHEMA_MAPPING = {
    # Boolean Fields
    fields.BooleanField: {'type': 'boolean'},
    fields.NullBooleanField: {'type': 'boolean'},
    # String Fields
    fields.CharField: {'type': 'string'},
    fields.EmailField: {
        'type': 'string',
        'pattern': '^\\S+@\\S+$',
        'validationMessage': 'Please enter a valid email address.'
    },
    fields.RegexField: {'type': 'string'},
    fields.SlugField: {'type': 'string'},
    fields.URLField: {'type': 'string'},
    fields.UUIDField: {'type': 'string'},
    fields.FilePathField: {'type': 'string'},
    fields.IPAddressField: {'type': 'string'},
    # Numeric Fields
    fields.IntegerField: {'type': 'integer'},
    fields.FloatField: {'type': 'number'},
    fields.DecimalField: {'type': 'number'},
    # Date and time fields
    fields.DateTimeField: {'type': 'string', 'format': 'datetimepicker'},
    fields.DateField: {'type': 'string', 'format': 'datepicker'},
    fields.TimeField: {'type': 'string', 'format': 'timepicker'},
    # Choice selection fields
    fields.ChoiceField: {'type': 'string'},
    fields.MultipleChoiceField: {'type': 'string'},
    # File upload fields
    fields.FileField: {'type': 'string'},
    fields.ImageField: {'type': 'string'},
    # Composite fields
    fields.ListField: {'type': 'array'},
    fields.DictField: {'type': 'object'},
    # Miscellaneous fields
    fields.ReadOnlyField: {'type': 'string'},
    fields.HiddenField: {'type': 'string'},
    fields.ModelField: {'type': 'string'},
    fields.SerializerMethodField: {'type': 'string'},
}
