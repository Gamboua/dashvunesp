# -*- coding: utf-8 -*-
from __future__ import unicode_literals

###############################################
# Incluindo Models & Serializers
###############################################
from curso.models import Curso,Matricula
from curso.serializers import CursoSerializer,MatriculaSerializer

###############################################
# Incluindo Bibliotecas do Django Rest
###############################################
from rest_framework import viewsets

###############################################
# Views de API
###############################################

class CursoApiView(viewsets.ModelViewSet):

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaApiView(viewsets.ModelViewSet):

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer