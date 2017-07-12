# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from curso.serializers import MatriculaMongoSerializer
from curso.models import MatriculaMongo
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet


class MatriculaMongoView(MongoModelViewSet):

    queryset = MatriculaMongo.objects.all()
    serializer_class = MatriculaMongoSerializer
