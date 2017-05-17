#!/usr/bin/python
#-*- coding: utf-8 -*-

"""efigie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import include, url
# from django.conf.urls import (
#   handler400, handler403, handler404, handler500
# )
from django.contrib import admin
import efigie.views 


urlpatterns = [
  url(r'^$', efigie.views.index, name='index'),
  url(r'^about/', efigie.views.about, name='about'),

  url(r'^login/$', efigie.views.userLogin, name='userLogin'),
  url(r'^logout/$', efigie.views.userLogout, name='userLogout'),

  url(r'^user/new/$', efigie.views.userNew, name='userNew'),
  url(r'^user/new/(?P<key>\w+)/$', efigie.views.userNewConfirm, name='userNewConfirm'),

  url(r'^user/password/forget/$', efigie.views.userPasswordReset, name='userPasswordReset'),
  url(r'^user/password/forget/(?P<key>\w+)/$', efigie.views.userPasswordResetConfirm, name='userPasswordResetConfirm'),
  
  url(r'^user/settings/$', efigie.views.userSettings, name='userSettings'),
  url(r'^user/delete/$', efigie.views.userDelete, name='userDelete'),
  url(r'^user/settings/password/$',  efigie.views.userPasswordEdit, name='userPasswordEdit'),

  url(r'^user/settings/profile/$',  efigie.views.userEdit, name='userEdit'),
  url(r'^user/settings/profile/(?P<key>\w+)/$',  efigie.views.userEditConfirm, name='userEditConfirm'),

  url(r'^key/new/$', efigie.views.keyNew, name='keyNew'),
  url(r'^key/list/$', efigie.views.keyList, name='keyList'),
  url(r'^key/import/$', efigie.views.keyImport, name='keyImport'),

  url(r'^key/(?P<keyId>[0-9]+)/show/$', efigie.views.keyShow, name='keyShow'),
  url(r'^key/(?P<keyId>[0-9]+)/edit/$', efigie.views.keyEdit, name='keyEdit'),
  url(r'^key/(?P<keyId>[0-9]+)/delete/$', efigie.views.keyDelete, name='keyDelete'),
  url(r'^key/(?P<keyId>[0-9]+)/export/$', efigie.views.keyExport, name='keyExport'),



  # url(r'^criar-conta/$', efigie.views.register, name='register'),
  # url(r'^nova-senha/$', efigie.views.password_reset, name='password_reset'),
  # url(r'^$', efigie.views.index, name='index'),
  # url(r'^admin/', admin.site.urls),
]

# handler400 = efigie.views.errorViews.bad_request
# handler403 = efigie.views.errorViews.permission_denied
# handler404 = efigie.views.errorViews.page_not_found
# handler500 = efigie.views.errorViews.server_error


def breadcrumbResolve(url_name):
  urls = [
    {'name': 'index', 'title': 'Home', 'icon': 'fa-home'},
    {'name': 'about', 'title': 'Sobre', 'icon': 'fa-info-circle'},
    {'name': 'userLogin', 'title': 'Login', 'icon': 'a-sign-in'},
    {'name': 'userLogout', 'title': 'Logout', 'icon': 'fa-sign-out'},
    {'name': 'userNew', 'title': 'Cadastrar Usuário', 'icon': 'fa-user-plus'},
    {'name': 'userNewConfirm', 'title': 'Confirmar Usuário', 'icon': 'fa-user-plus'},
    {'name': 'userPasswordReset', 'title': 'Restaurar Senha', 'icon': 'fa-lock'},
    {'name': 'userPasswordResetConfirm', 'title': 'Confirmar Senha', 'icon': 'fa-lock'},
    {'name': 'userSettings', 'title': 'Exibir Dados da Conta', 'icon': 'fa-list-alt'},
    {'name': 'userDelete', 'title': 'Deletar Usuário', 'icon': 'fa-user-times'},
    {'name': 'userPasswordEdit', 'title': 'Editar Senha', 'icon': 'fa-lock'},
    {'name': 'userEdit', 'title': 'Editar Usuário', 'icon': 'fa-user'},
    {'name': 'userEditConfirm', 'title': 'Confirmar Edição de Usuário', 'icon': 'fa-user'},
    {'name': 'keyNew', 'title': 'Criar Chave', 'icon': 'fa-plus'},
    {'name': 'keyList', 'title': 'Listar Chaves', 'icon': 'fa-list'},
    {'name': 'keyImport', 'title': 'Importar Chave', 'icon': 'fa-upload'},
    {'name': 'keyShow', 'title': 'Exibir Chave', 'icon': 'fa-list-alt'},
    {'name': 'keyEdit', 'title': 'Editar Chave', 'icon': 'fa-pencil'},
    {'name': 'keyDelete', 'title': 'Deletar Chave', 'icon': 'fa-times'},
    {'name': 'keyExport', 'title': 'Exportar Chave', 'icon': 'fa-download'},
  ]

  for url in urls:
    if url['name'] == url_name:
      return url['title'], url['icon']