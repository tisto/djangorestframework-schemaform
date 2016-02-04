# -*- coding: utf-8 -*-
from django.db import models  # noqa
from rest_framework_schemaform.models import Application  # noqa
from uuid import uuid4


class User(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4)
    loginname = models.CharField(max_length=200, unique=True)
    firstname = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    mobil = models.CharField(max_length=100, null=True, blank=True)
    lastlogin = models.DateTimeField(null=True, blank=True)
    salutation = models.ForeignKey(Application, null=True)
