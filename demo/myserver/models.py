# -*- coding: utf-8 -*-
from django.db import models


class Application(models.Model):

    title = models.CharField(
        u'Title',
        help_text=u'Title of the application',
        max_length=255
    )
