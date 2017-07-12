# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from aluno.serializers import AlunoMongoSerializer
from django.views.decorators.http import require_GET
from aluno.models import AlunoMongo
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet


class AlunoMongoView(MongoModelViewSet):

    queryset = AlunoMongo.objects.all()
    serializer_class = AlunoMongoSerializer
