# -*- coding: utf-8 -*-
# Generated by Django 1.9c1 on 2015-11-20 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the application', max_length=255, verbose_name='Title')),
                ('description', models.TextField(blank=True, help_text='Description of the application', null=True, verbose_name='Description')),
                ('salutation', models.CharField(blank=True, choices=[('mr', 'Mr'), ('mrs', 'Mrs'), ('ms', 'Ms')], max_length=255, null=True, verbose_name='Salutation')),
                ('username', models.CharField(help_text='External validation, anything but "Bob" is valid.', max_length=255, null=True, verbose_name='Username')),
                ('firstname', models.CharField(help_text='Your first name', max_length=255, verbose_name='First name')),
                ('lastname', models.CharField(help_text='Your last name', max_length=255, verbose_name='Last name')),
                ('street', models.CharField(help_text='Your street name', max_length=255, null=True, verbose_name='Street')),
                ('house_number', models.CharField(max_length=255, null=True, verbose_name='House number')),
                ('zip_number', models.CharField(max_length=5, null=True, verbose_name='ZIP number')),
                ('city', models.CharField(max_length=255, null=True, verbose_name='City')),
                ('country', models.CharField(max_length=255, null=True, verbose_name='Country')),
                ('email', models.EmailField(blank=True, help_text='Your email address', max_length=254, null=True, verbose_name='Email address')),
                ('age', models.IntegerField(blank=True, help_text='Your age', null=True, verbose_name='Age')),
                ('date', models.DateField(auto_now=True, help_text='Example of a Django DateField with a date picker', null=True, verbose_name='Date')),
                ('datetime', models.DateTimeField(auto_now=True, help_text='Example of a Django DateTimeField with a datetime picker', null=True, verbose_name='Datetime')),
                ('time', models.TimeField(auto_now=True, help_text='Example of a Django TimeField with a time picker', null=True, verbose_name='Time')),
                ('start_date', models.DateField(auto_now=True, help_text='Start date needs to be before end date.', null=True, verbose_name='Start date')),
                ('end_date', models.DateField(auto_now=True, help_text='End date needs to be after start date.', null=True, verbose_name='End date')),
                ('attachment', models.FileField(blank=True, help_text='File attachment', null=True, upload_to='', verbose_name='Attachment')),
                ('image', models.ImageField(blank=True, help_text='Image attachment', null=True, upload_to='', verbose_name='Image')),
                ('url', models.URLField(blank=True, help_text='URL help text', null=True, verbose_name='URL')),
                ('uuid', models.UUIDField(blank=True, help_text='UUID help text', null=True, verbose_name='UUID')),
                ('gender', models.CharField(blank=True, choices=[('m', 'male'), ('f', 'female')], help_text='Gender help text', max_length=6, null=True, verbose_name='Gender')),
                ('first_time_application', models.NullBooleanField(help_text='Is this your first time application?', verbose_name='First time application')),
                ('first_time_application_reason', models.CharField(max_length=255, null=True, verbose_name='Reason for first time application')),
            ],
        ),
    ]
