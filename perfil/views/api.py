# -*- coding: utf-8 -*-
from __future__ import unicode_literals

###############################################
# Incluindo Models & Serializers
###############################################
from perfil.models import Perfil,PerfilCurso,PerfilAluno
from perfil.serializers import PerfilSerializer, PerfilAlunoSerializer, PerfilCursoSerializer

###############################################
# Incluindo Bibliotecas do Django Rest
###############################################
from rest_framework import viewsets

###############################################
# Views de API
###############################################

class PerfilApiView(viewsets.ModelViewSet):

    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer


class PerfilApiAlunoView(viewsets.ModelViewSet):

    queryset = PerfilAluno.objects.all()
    serializer_class = PerfilAlunoSerializer


class PerfilApiCursoView(viewsets.ModelViewSet):

    queryset = PerfilCurso.objects.all()
    serializer_class = PerfilCursoSerializer