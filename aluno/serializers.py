from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import Aluno, AlunoMongo
from perfil.models import Perfil

class AlunoSerializer(serializers.ModelSerializer):

    perfil_aluno = serializers.PrimaryKeyRelatedField(many=True,queryset=Perfil.objects.all())

    class Meta(object):
        model = Aluno
        fields = '__all__'


class AlunoMongoSerializer(DocumentSerializer):

    class Meta(object):
        model = AlunoMongo
        fields = '__all__'