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
<<<<<<< HEAD
  url(r'^$', efigie.views.index, name='index', 
    kwargs={'title': 'Home', 'icon': 'fa-home'}),
  url(r'^about/', efigie.views.about, name='about', 
    kwargs={'title': 'Sobre', 'icon': 'fa-info-circle'}),
=======
  url(r'^$', efigie.views.index, name='index', kwargs={'title': 'Home', 'icon': 'fa-info-circle'}),
  url(r'^about/', efigie.views.about, name='about', kwargs={'title': 'Sobre', 'icon': 'fa-info-circle'}),
>>>>>>> master

  url(r'^login/$', efigie.views.userLogin, name='userLogin', 
    kwargs={'title': 'Login', 'icon': 'a-sign-in'}),
  url(r'^logout/$', efigie.views.userLogout, name='userLogout', 
    kwargs={'title': 'Logout', 'icon': 'fa-sign-out'}),

  url(r'^user/new/$', efigie.views.userNew, name='userNew',
    kwargs={'title': 'Criar Usuário', 'icon': 'fa-user-plus'}),
  url(r'^user/new/(?P<key>\w+)/$', efigie.views.userNewConfirm, name='userNewConfirm', 
    kwargs={'title': 'Confirmar Usuário', 'icon': 'fa-user-plus'}),

  url(r'^user/password/forget/$', efigie.views.userPasswordReset, name='userPasswordReset', 
    kwargs={'title': 'Restaurar Senha', 'icon': 'fa-lock'}),
  url(r'^user/password/forget/(?P<key>\w+)/$', efigie.views.userPasswordResetConfirm, name='userPasswordResetConfirm', 
    kwargs={'title': 'Confirmar Senha', 'icon': 'fa-lock'}),
  
  url(r'^user/settings/$', efigie.views.userSettings, name='userSettings', 
    kwargs={'title': 'Exibir Dados da Conta', 'icon': 'fa-list-alt'}),
  url(r'^user/delete/$', efigie.views.userDelete, name='userDelete', 
    kwargs={'title': 'Deletar Usuário', 'icon': 'fa-user-times'}),
  url(r'^user/settings/password/$',  efigie.views.userPasswordEdit, name='userPasswordEdit', 
    kwargs={'title': 'Editar Senha', 'icon': 'fa-lock'}),

  url(r'^user/settings/profile/$',  efigie.views.userEdit, name='userEdit', 
    kwargs={'title': 'Editar Usuário', 'icon': 'fa-user'}),
  url(r'^user/settings/profile/(?P<key>\w+)/$',  efigie.views.userEditConfirm, name='userEditConfirm', 
    kwargs={'title': 'Confirmar Edição de Usuário', 'icon': 'fa-user'}),

  url(r'^key/new/$', efigie.views.keyNew, name='keyNew', 
    kwargs={'title': 'Criar Senha', 'icon': 'fa-plus'}),
  url(r'^key/list/$', efigie.views.keyList, name='keyList', 
    kwargs={'title': 'Listar Chaves', 'icon': 'fa-list'}),
  url(r'^key/import/$', efigie.views.keyImport, name='keyImport', 
    kwargs={'title': 'Importar Chaves', 'icon': 'fa-upload'}),

  url(r'^key/(?P<keyId>[0-9]+)/show/$', efigie.views.keyShow, name='keyShow', 
    kwargs={'title': 'Exibir Chave', 'icon': 'fa-list-alt'}),
  url(r'^key/(?P<keyId>[0-9]+)/edit/$', efigie.views.keyEdit, name='keyEdit', 
    kwargs={'title': 'Editar Chave', 'icon': 'fa-pencil'}),
  url(r'^key/(?P<keyId>[0-9]+)/delete/$', efigie.views.keyDelete, name='keyDelete', 
    kwargs={'title': 'Deletar Chave', 'icon': 'fa-times'}),
  url(r'^key/(?P<keyId>[0-9]+)/export/$', efigie.views.keyExport, name='keyExport', 
    kwargs={'title': 'Exportar Chave', 'icon': 'fa-download'}),



  # url(r'^criar-conta/$', efigie.views.register, name='register'),
  # url(r'^nova-senha/$', efigie.views.password_reset, name='password_reset'),
  # url(r'^$', efigie.views.index, name='index'),
  # url(r'^admin/', admin.site.urls),
]

# handler400 = efigie.views.errorViews.bad_request
# handler403 = efigie.views.errorViews.permission_denied
# handler404 = efigie.views.errorViews.page_not_found
# handler500 = efigie.views.errorViews.server_error