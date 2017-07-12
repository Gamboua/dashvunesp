# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mongoengine import *

# Create your models here.
class Aluno(models.Model):

    class Meta(object):
        ordering = ['-id']
        db_table = 'aluno'

    nome = models.CharField(max_length=50, blank=False)
    sobrenome = models.CharField(max_length=100, blank=False)
    cpf = models.CharField(max_length=14, blank=False)
    email = models.CharField(max_length=100, blank=False, unique=True)
    idNumber = models.IntegerField(blank=False)

    perfil_aluno = models.ManyToManyField('perfil.Perfil',through='perfil.PerfilAluno')



connect('teste')


class AlunoMongo(Document):
   nome = StringField(max_length=50)
   sobrenome = StringField(max_length=100)
   cpf = StringField()
   email = EmailField()
   perfis = ListField()
   action = StringField()
   idnumber = IntField()
