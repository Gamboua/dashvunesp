# -*- coding: utf-8 -*-
from __future__ import unicode_literals

###############################################
# Incluindo Models & Forms
###############################################
from curso.models import Curso
from curso.forms import CursoForm
from moodle.models import MdlCourse

###############################################
# Incluindo Bibliotecas do Django Base
###############################################
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

###############################################
# Views do Dashboard
###############################################

@login_required
def CursoIndex(request):
    curso = Curso.objects.all()
    return render(request,"cursos/index.html", {"curso":curso} )


@login_required
def CursoInserirView(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Curso cadastrado com sucesso!")
            return HttpResponseRedirect("/cursos/")
        else:
            messages.error(request,"Falha ao cadastrar um novo curso - Um ou mais campos estão inválidos")
    return render(request,"cursos/new.html")


@login_required
def CursoEditarView(request,idCurso):
    curso = get_object_or_404(Curso, pk=idCurso)
    if request.method == "POST":
        form = CursoForm(request.POST or None,instance=curso)
        if form.is_valid():
            form.save()
            messages.success(request, "Curso atualizado com sucesso!")
            return HttpResponseRedirect("/cursos/")
        else:
            messages.error(request,"Falha ao atualizar o curso {0} - Um ou mais campos estão inválidos".format(curso.nome))
    return render(request, "cursos/edit.html",{"curso":curso})

@login_required
def CursoShowView(request,idCurso):
    curso = get_object_or_404(Curso, pk=idCurso)

    matriculas = curso.matricula_set.all()

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

    return render(request, "cursos/view.html",{"curso":curso, 'matriculas': matriculas})

@login_required
def CursoExcluirView(request,idCurso):
    curso = get_object_or_404(Curso, pk=idCurso)
    if curso != None:
        curso.delete()
        messages.success(request, "Curso removido com sucesso!")
    else:
        messages.warning(request, "Curso não localizado".format(perfil.nome))
    return HttpResponseRedirect("/perfil/")