# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
        ('curso', '0001_initial'),
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='matriculas',
            field=models.ManyToManyField(through='curso.Matricula', to='curso.Curso'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='perfil_aluno',
            field=models.ManyToManyField(through='perfil.PerfilAluno', to='perfil.Perfil'),
        ),
    ]
