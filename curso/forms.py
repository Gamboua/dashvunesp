from django import forms
from .models import Curso, Matricula

class CursoForm(forms.ModelForm):

    class Meta(object):
        model = Curso
        fields = ['nome']

class MatriculaForm(forms.ModelForm):

    class Meta(object):
        model = Matricula
        fields = '__all__'