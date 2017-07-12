# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Perfil(models.Model):

    class Meta(object):
        ordering = ['-id']
        db_table = 'perfil'

    nome = models.CharField(max_length=50, blank=False)
    descricao = models.CharField(max_length=100, blank=True)
    perfil_aluno = models.ManyToManyField('aluno.Aluno',through='PerfilAluno')
    perfil_curso = models.ManyToManyField('curso.Curso',through='PerfilCurso')

    def __unicode__(self):
        return self.nome


class PerfilAluno(models.Model):

    class Meta(object):
        ordering = ['-id']
        db_table ='perfil_aluno'
        auto_created = True

    perfil = models.ForeignKey(Perfil,on_delete=models.CASCADE)
    aluno = models.ForeignKey('aluno.Aluno',on_delete=models.CASCADE)

class PerfilCurso(models.Model):

    class Meta(object):
        ordering = ['-id']
        db_table = 'perfil_curso'
        auto_created = True

    perfil = models.ForeignKey(Perfil,on_delete=models.CASCADE)
    curso = models.ForeignKey('curso.Curso',on_delete=models.CASCADE)