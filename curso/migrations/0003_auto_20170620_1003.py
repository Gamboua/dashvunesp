# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 13:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0002_curso_perfil_curso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matricula',
            old_name='aluno_id',
            new_name='aluno',
        ),
        migrations.RenameField(
            model_name='matricula',
            old_name='curso_id',
            new_name='curso',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='matriculas',
        ),
    ]