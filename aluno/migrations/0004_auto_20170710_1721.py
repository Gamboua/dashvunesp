# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0003_remove_aluno_matriculas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        )
    ]
