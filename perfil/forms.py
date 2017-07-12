from django import forms
from .models import Perfil, PerfilAluno, PerfilCurso

class PerfilForm(forms.ModelForm):

    class Meta(object):
        model = Perfil
        fields = ['nome']

class PerfilAlunoForm(forms.ModelForm):

    class Meta(object):
        model = PerfilAluno
        fields = '__all__'

class PerfilCursoForm(forms.ModelForm):

    class Meta(object):
        model = PerfilCurso
        fields = '__all__'