# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 17:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0004_remove_curso_moodle_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='perfil_curso',
        ),
    ]