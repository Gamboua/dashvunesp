from rest_framework import serializers
from .models import Curso, Matricula, MatriculaMongo
from rest_framework_mongoengine.serializers import DocumentSerializer
from perfil.models import Perfil

class CursoSerializer(serializers.ModelSerializer):

    perfil_curso = serializers.PrimaryKeyRelatedField(many=True,queryset=Perfil.objects.all())

    class Meta(object):
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Matricula
        fields = '__all__'

class MatriculaMongoSerializer(DocumentSerializer):

    class Meta(object):
        model = MatriculaMongo
        fields = '__all__'