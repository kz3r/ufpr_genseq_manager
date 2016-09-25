"""ufpr_genseq_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

#Removido uso do _nested* - Verificar efeito colateral
#from rest_framework_nested import routers
from rest_framework import routers
from genseq.views import UsuarioViewSet, ServicoViewSet, SistemaViewSet, KitDeplecaoViewSet,LoginView, LogoutView, InstituicaoViewSet, ProjetoViewSet, UsuarioProjetoViewSet, PapelProjetoViewSet, AmostraViewSet, ProjetoAmostraViewSet

router = routers.SimpleRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'servicos', ServicoViewSet)
router.register(r'sistemas', SistemaViewSet)
router.register(r'kit_deplecao', KitDeplecaoViewSet)
router.register(r'instituicao', InstituicaoViewSet)
router.register(r'projeto', ProjetoViewSet)
router.register(r'usuarioprojeto', UsuarioProjetoViewSet)
router.register(r'papelprojeto', PapelProjetoViewSet)
router.register(r'amostra', AmostraViewSet)
router.register(r'projetoamostra', ProjetoAmostraViewSet)


urlpatterns = [
	url(r'^genseq_api/', include(router.urls)),
    url(r'^genseq_api/login/$', LoginView.as_view(), name='login'),
    url(r'^genseq_api/logout/$', LogoutView.as_view(), name='logout'),
    url(r'^admin/', include(admin.site.urls)),
]
