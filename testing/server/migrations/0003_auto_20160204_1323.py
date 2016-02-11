# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-04 13:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rest_framework_schemaform', '__first__'),
        ('server', '0002_auto_20151126_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('loginname', models.CharField(max_length=200, unique=True)),
                ('firstname', models.CharField(blank=True, max_length=100, null=True)),
                ('lastname', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('mobil', models.CharField(blank=True, max_length=100, null=True)),
                ('lastlogin', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Application',
        ),
        migrations.AddField(
            model_name='user',
            name='salutation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rest_framework_schemaform.Application'),
        ),
    ]