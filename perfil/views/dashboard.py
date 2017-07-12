# -*- coding: utf-8 -*-
from __future__ import unicode_literals

###############################################
# Incluindo Models, Forms & Serializers
###############################################
from perfil.models import Perfil, PerfilCurso
from perfil.forms import PerfilForm
from curso.models import Curso

###############################################
# Incluindo Bibliotecas do Django Rest
###############################################
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

###############################################
# Views do Dashboard
###############################################

@login_required
def PerfilIndexView(request):
    perfil = Perfil.objects.all()
    return render(request, "perfis/index.html", {"perfil": perfil})


@login_required
def PerfilCriarView(request):
    if request.method == "POST":
        form = PerfilForm(request.POST)
        if form.is_valid():
            pcurso = form.save(commit=True)
            for pc in request.POST.getlist('curso'):
                curso = get_object_or_404(Curso, pk=pc)
                pcursoform = PerfilCurso()
                pcursoform.curso = curso
                pcursoform.perfil = pcurso
                pcursoform.save()
            messages.success(request, "Perfil cadastrado com sucesso!")
            return HttpResponseRedirect("/perfil/")
        else:
            messages.error(request, "Falha ao cadastrar um novo perfil - Um ou mais campos estão inválidos")
    curso = Curso.objects.all()
    return render(request, "perfis/new.html", {"curso": curso})


@login_required
def PerfilEditarView(request,idPerfil):
    perfil = get_object_or_404(Perfil,pk=idPerfil)
    curso = Curso.objects.all()
    if request.method == "POST":
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            pcurso = form.save()
            PerfilCurso.objects.filter(perfil_id=idPerfil).delete()
            for pc in request.POST.getlist('curso'):
                curso = get_object_or_404(Curso, pk=pc)
                pcursoform = PerfilCurso()
                pcursoform.curso = curso
                pcursoform.perfil = pcurso
                pcursoform.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return HttpResponseRedirect("/perfil/")
        else:
            messages.error(request,"Falha ao atualizar o perfil {0} - Um ou mais campos estão inválidos".format(perfil.nome))
    return render(request,"perfis/edit.html",{"curso": curso, "perfil": perfil})

@login_required
def PerfilExcluirView(request,idPerfil):
    perfil = get_object_or_404(Perfil,pk=idPerfil)
    if perfil != None:
        perfil.delete()
        messages.success(request, "Perfil removido com sucesso!")
    else:
        messages.warning(request,"Perfil não localizado".format(perfil.nome))
    return HttpResponseRedirect("/perfil/")