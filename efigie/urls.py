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
from django.contrib import admin
from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _

import efigie.views as views


urlpatterns = [
  # url(r'^i18n/', include('django.conf.urls.i18n')),
  # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
  # url(r'^admin/', admin.site.urls),

  url(r'^$', views.index, name='index'),

  url(r'^key/$', views.keyList, name='keyList'),
  url(r'^key/new/$', views.keyNew, name='keyNew'),
  url(r'^key/(?P<keyId>[0-9]+)/$', views.keyShow, name='keyShow'),
  url(r'^key/(?P<keyId>[0-9]+)/edit/$', views.keyEdit, name='keyEdit'),
  url(r'^key/(?P<keyId>[0-9]+)/delete/$', views.keyDelete, name='keyDelete'),
  url(r'^key/(?P<keyId>[0-9]+)/export/$', views.keyExport, name='keyExport'),
  url(r'^key/import/$', views.keyImport, name='keyImport'),


]

def breadcrumbResolve(url_name):
  urls = [
    {'name': 'index', 'title': _('Home'), 'icon': 'fa-home'},

    {'name': 'keyList', 'title': _("Key's List"), 'icon': 'fa-list'},
    {'name': 'keyNew', 'title': _('New Key'), 'icon': 'fa-plus'},
    {'name': 'keyShow', 'title': _('Key'), 'icon': 'fa-home'},
    {'name': 'keyEdit', 'title': _('Edit Key'), 'icon': 'fa-pencil'},
    {'name': 'keyDelete', 'title': _('Delete Key'), 'icon': 'fa-trash-o'},
    {'name': 'keyExport', 'title': _('Export Key'), 'icon': 'fa-download'},
    {'name': 'keyImport', 'title': _('Import Key'), 'icon': 'fa-upload'},

  ]

  for url in urls:
    if url['name'] == url_name:
      return url['title'], url['icon']

  return 'NEED TO ADD TITLE %s' % (url_name), ' '
