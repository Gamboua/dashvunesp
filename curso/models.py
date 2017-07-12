# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mongoengine import *
from moodle.models import MdlGradeGrades, MdlGradeItems, MdlUser, MdlCourse

# Create your models here.
class Curso(models.Model):

    class Meta:
        ordering = ['-id']
        db_table = 'curso'

    nome = models.CharField(max_length=50,blank=False)
    descricao = models.CharField(max_length=100, blank=True)

class Matricula(models.Model):

    class Meta:
        ordering = ['-id']
        db_table = 'matricula'

    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    aluno = models.ForeignKey('aluno.Aluno',on_delete=models.CASCADE)
    nota = models.IntegerField(blank=False,default=0)

    def get_progresso(self):
        user = self.get_user_moodle()

        # todas as atividades do curso
        total_atividades = MdlGradeItems.objects.using('moodle').all().filter(courseid=self.get_curso_moodle().id).exclude(itemname=None)

        total_atividades_concluidas = []
        for atv in total_atividades:
            atividade = MdlGradeGrades.objects.using('moodle').filter(userid=user.id, itemid=atv.id, aggregationstatus='used').first()
            if atividade:
                total_atividades_concluidas.append(atividade)

        progresso =  {
            "progresso": int((float(len(total_atividades_concluidas)) / float(len(total_atividades)) * 100)),
            "min": len(total_atividades_concluidas),
            "max": len(total_atividades)
        }

        return progresso

    def get_media(self):
        user = self.get_user_moodle()

        total_atividades = MdlGradeItems.objects.using('moodle').all().filter(courseid=self.get_curso_moodle().id).exclude(itemname=None)

        notas = []
        for atv in total_atividades:
            atividade = MdlGradeGrades.objects.using('moodle').filter(userid=user.id, itemid=atv.id, aggregationstatus='used').first()
            if atividade:
                notas.append(atividade)

        return sum([ n.finalgrade for n in notas ]) / len(total_atividades)

    def get_nota_final(self):
        user = self.get_user_moodle()

        total_atividades = MdlGradeItems.objects.using('moodle').all().filter(courseid=self.get_curso_moodle().id).exclude(itemname=None)

        notas = []
        for atv in total_atividades:
            atividade = MdlGradeGrades.objects.using('moodle').filter(userid=user.id, itemid=atv.id, aggregationstatus='used').first()
            if atividade:
                notas.append(atividade)

        return sum([ n.finalgrade for n in notas ])


    def get_curso_moodle(self):
        return MdlCourse.objects.using('moodle').get(idnumber=self.curso.id)

    def get_user_moodle(self):
        return MdlUser.objects.using('moodle').get(email=self.aluno.email)


connect('teste')
class MatriculaMongo(Document):
   curso = IntField(max_length=5)
   aluno = IntField(max_length=50)
   action = StringField()