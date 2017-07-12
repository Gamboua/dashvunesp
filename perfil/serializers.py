from rest_framework import serializers
from .models import Perfil, PerfilAluno, PerfilCurso

class PerfilSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Perfil
        fields = '__all__'

class PerfilAlunoSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = PerfilAluno
        fields = '__all__'

class PerfilCursoSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = PerfilCurso
        fields = '__all__'