# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myserver', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='age',
        ),
        migrations.RemoveField(
            model_name='application',
            name='attachment',
        ),
        migrations.RemoveField(
            model_name='application',
            name='city',
        ),
        migrations.RemoveField(
            model_name='application',
            name='country',
        ),
        migrations.RemoveField(
            model_name='application',
            name='date',
        ),
        migrations.RemoveField(
            model_name='application',
            name='datetime',
        ),
        migrations.RemoveField(
            model_name='application',
            name='description',
        ),
        migrations.RemoveField(
            model_name='application',
            name='email',
        ),
        migrations.RemoveField(
            model_name='application',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='application',
            name='first_time_application',
        ),
        migrations.RemoveField(
            model_name='application',
            name='first_time_application_reason',
        ),
        migrations.RemoveField(
            model_name='application',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='application',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='application',
            name='house_number',
        ),
        migrations.RemoveField(
            model_name='application',
            name='image',
        ),
        migrations.RemoveField(
            model_name='application',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='application',
            name='salutation',
        ),
        migrations.RemoveField(
            model_name='application',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='application',
            name='street',
        ),
        migrations.RemoveField(
            model_name='application',
            name='time',
        ),
        migrations.RemoveField(
            model_name='application',
            name='url',
        ),
        migrations.RemoveField(
            model_name='application',
            name='username',
        ),
        migrations.RemoveField(
            model_name='application',
            name='uuid',
        ),
        migrations.RemoveField(
            model_name='application',
            name='zip_number',
        ),
    ]
