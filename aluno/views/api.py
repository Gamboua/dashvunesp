# -*- coding: utf-8 -*-
from __future__ import unicode_literals

###############################################
# Incluindo Models & Serializers
###############################################
from aluno.models import Aluno, AlunoMongo
from curso.models import Matricula, Curso, MatriculaMongo
from perfil.models import Perfil
from aluno.serializers import AlunoSerializer

###############################################
# Incluindo Bibliotecas do Django Rest
###############################################
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

# Create your views here.

###############################################
# Views de API
###############################################
class AlunoApiView(viewsets.ModelViewSet):

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    def create(self, request, *args, **kwargs):

        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            self.create_aluno_mongo(request.data)
        except Exception as e:
            pass
        finally:
            headers = self.get_success_headers(serializer.data)

            for id in request.data.get('perfil_aluno'):
                perfil = Perfil.objects.get(pk=id)

                for cur in perfil.perfil_curso.all():
                    curso = Curso.objects.get(pk=cur.id)
                    aluno = Aluno.objects.get(email=serializer.data.get('email'))

                    try:
                        Matricula.objects.get(curso=curso, aluno=aluno)
                    except Exception as e:
                        matricula = Matricula(
                            curso=curso,
                            aluno=aluno
                        )
                        matricula.save()
                        self.create_matricula_mongo(curso.id, aluno.idNumber)


            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def create_aluno_mongo(self, data):
        mongo = AlunoMongo()
        mongo.nome = data.get('nome')
        mongo.sobrenome = data.get('sobrenome')
        mongo.email = data.get('email')
        mongo.cpf = data.get('cpf')
        mongo.action = 'insert'
        mongo.idnumber = data.get('idNumber')
        mongo.perfis = data.get('perfil_aluno')

        mongo.save()

    def create_matricula_mongo(self, curso, aluno):
        mongo = MatriculaMongo()
        mongo.curso = curso
        mongo.aluno = aluno
        mongo.action = 'insert'

        mongo.save()