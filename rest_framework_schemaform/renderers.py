# -*- coding: utf-8 -*-
from rest_framework import renderers
from .serializers import JsonSchemaSerializer

import json


class JSONSchemaRenderer(renderers.JSONRenderer):
    media_type = 'application/schema+json'
    format = 'schema+json'
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        # Look up the Django model
        view = renderer_context.get('view')
        queryset = view.get_queryset()
        model = queryset.model
        instance = model()
        # Pass the Django model to the serializer
        serializer = JsonSchemaSerializer(instance=instance)
        # Render the serializer result to json
        result = serializer.to_representation(data)
        return json.dumps(result)
