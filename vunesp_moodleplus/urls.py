"""vunesp_moodleplus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

###############################################
# Caminho default da template login.html
###############################################
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGIN_DIR = {'template_name': os.path.join(BASE_DIR, 'templates/index.html')}

###############################################
# Importando bibliotecas do Django
###############################################
from django.conf.urls import url, include
from django.contrib.auth import views as django_views

###############################################
# Importando bibliotecas do Rest API
###############################################
from rest_framework import routers
from rest_framework.authtoken import views as rest_views
from rest_framework_mongoengine import routers as mongo_routers

# Importando Apps de Aluno, Curso e Perfil
from aluno import views as aluno_views
from curso import views as curso_views
from perfil import views as perfil_views

###############################################
# Importando Apps de Aluno, Curso, Index & Perfil
###############################################
from aluno import views as aluno_views
from curso import views as curso_views
from perfil import views as perfil_views

###############################################
# Criando rotas para a API
###############################################
mongo_router = mongo_routers.SimpleRouter()
routerApi = routers.DefaultRouter()

# Informando as rotas da API - Aluno
routerApi.register(r'aluno', aluno_views.AlunoApiView)
mongo_router.register(r'aluno',aluno_views.AlunoMongoView, 'Aluno')
mongo_router.register(r'matricula',curso_views.MatriculaMongoView, 'Aluno')

# Informando as rotas da API - Curso
routerApi.register(r'curso',curso_views.CursoApiView)
routerApi.register(r'matricula',curso_views.MatriculaApiView)

# Informando as rotas da API - Perfil
routerApi.register(r'perfil',perfil_views.PerfilApiView)
routerApi.register(r'perfil_aluno',perfil_views.PerfilApiAlunoView)
routerApi.register(r'perfil_curso',perfil_views.PerfilApiCursoView)

###############################################
# Incluindo URLs
###############################################
urlpatterns = [

    ###########################################
    # Urls da API da Vunesp
    ###########################################
    url(r'^api/', include(routerApi.urls)),
    url(r'^api/moodle/', include(mongo_router.urls)),
    url(r'^api/',include('rest_framework.urls',namespace='rest_framework')),
    url(r'^api/auth/$',rest_views.obtain_auth_token),

    ###########################################
    # Urls da Tela de Alunos
    ###########################################
    url(r'^alunos/$',aluno_views.AlunoIndexView, name='aluno_index'),
    url(r'^alunos/(?P<idAluno>[0-9]+)/$',aluno_views.AlunoShowView),

    ###########################################
    # Urls da Tela de Cursos
    ###########################################
    url(r'^cursos/$',curso_views.CursoIndex, name='curso_index'),
    url(r'^cursos/novo/$',curso_views.CursoInserirView, name='curso_cadastrar'),
    url(r'^cursos/editar/(?P<idCurso>[0-9]+)/$',curso_views.CursoEditarView, name='curso_editar'),
    url(r'^cursos/(?P<idCurso>[0-9]+)/$',curso_views.CursoShowView, name='curso_view'),
    url(r'^cursos/excluir/(?P<idCurso>[0-9]+)/$',curso_views.CursoExcluirView, name='curso_excluir'),

    ###########################################
    # Urls da Tela de Perfis e Integracao
    ###########################################
    url(r'^perfil/$',perfil_views.PerfilIndexView,name="perfil_index"),
    url(r'^perfil/novo/$',perfil_views.PerfilCriarView,name="perfil_cadastrar"),
    url(r'^perfil/(?P<idPerfil>[0-9]+)/$',perfil_views.PerfilEditarView,name="perfil_editar"),
    url(r'^perfil/excluir/(?P<idPerfil>[0-9]+)/$', perfil_views.PerfilExcluirView, name="perfil_excluir"),

    ###########################################
    # Urls da Tela de Login
    ###########################################
    url(r'^$', django_views.login,LOGIN_DIR,name='login'),
    url(r'^logout/$', django_views.logout,LOGIN_DIR,name='logout'),
]
