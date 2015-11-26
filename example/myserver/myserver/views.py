# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from myserver.models import Application
from rest_framework_schemaform.serializers import JsonSchemaSerializer

from django.shortcuts import render_to_response


def index(request):
    return render_to_response(
        'myserver/index.html'
    )


class ApplicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows applications to be viewed or edited.
    """
    queryset = Application.objects.all()
    serializer_class = JsonSchemaSerializer

    def list(self, request):
        queryset = Application.objects.all()
        app = Application()
        serializer = JsonSchemaSerializer(app)
        return Response(serializer.data)

    def create(self, request):
        pass

    def detail(self, request, pk=None):
        pass

    def retrieve(self, request, pk=None):
        queryset = Application.objects.all()
        app = get_object_or_404(queryset, pk=pk)
        serializer = JsonSchemaSerializer(app)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
