from __future__ import unicode_literals

###############################################
# Incluindo Models & Serializers
###############################################
from aluno.models import Aluno
from moodle.models import MdlGradeItems, MdlCourse, MdlUser, MdlGradeGrades
###############################################
# Incluindo Bibliotecas do Django Base
###############################################
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

###############################################
# Views do Dashboard
###############################################
@login_required
def AlunoIndexView(request):
    aluno = Aluno.objects.all()
    return render(request,'alunos/index.html', {'aluno':aluno} )

@login_required
def AlunoShowView(request,idAluno):
    aluno = get_object_or_404(Aluno,pk=idAluno)
    matriculas = aluno.matricula_set.all()

    for mat in matriculas:
        try:
            notas = mat.get_progresso()
            mat.progresso = notas['progresso']
            mat.min = notas['min']
            mat.max = notas['max']
            mat.media = mat.get_media()
            mat.nota = mat.get_nota_final()
        except Exception as e:
            mat.progresso = None
            mat.min = 0
            mat.max = 0
            mat.media = 0.0
            mat.nota = 0.0

    return render(request,'alunos/view.html',   {'matriculas': matriculas, 'aluno': aluno} )
