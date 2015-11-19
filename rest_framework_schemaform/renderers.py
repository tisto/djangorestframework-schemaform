# -*- coding: utf-8 -*-
from rest_framework import renderers
from .serializers import JsonSchemaSerializer

import json


class JSONSchemaRenderer(renderers.JSONRenderer):
    media_type = 'application/schema+json'
    format = 'schema+json'
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        serializer = JsonSchemaSerializer()
        result = serializer.to_representation(data)
        return json.dumps(result)
