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

admin.site.site_header = 'Efigie Administration'

urlpatterns = [
  url(r'^i18n/', include('django.conf.urls.i18n')),
  url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
  url(r'^admin/', admin.site.urls),

  url(r'^$', views.index, name='index'),
  url(r'^about/$', views.about, name='about'),
  url(r'^settings/$', views.systemSettings, name='systemSettings'),

  url(r'^login/$', views.userLogin, name='userLogin'),
  url(r'^logout/$', views.userLogout, name='userLogout'),
  url(r'^user/new/$', views.userNew, name='userNew'),
  url(r'^user/new/(?P<token>\w+)/$', views.userConfirm, name='userNewConfirm'),

  url(r'^user/password/forget/$', views.userPasswordReset, name='userPasswordReset'),
  url(r'^user/password/forget/(?P<token>\w+)/$', views.userConfirm, name='userPasswordResetConfirm'),

  url(r'^user/settings/$', views.userSettings, name='userSettings'),
  url(r'^user/settings/password/$', views.userPasswordEdit, name='userPasswordEdit'),
  url(r'^user/settings/profile/$',  views.userEdit, name='userEdit'),
  url(r'^user/settings/profile/(?P<token>\w+)/$',  views.userConfirm, name='userEditConfirm'),

  url(r'^key/$', views.keyList, name='keyList'),
  url(r'^key/new/$', views.keyNew, name='keyNew'),
  url(r'^key/import/$', views.keyImport, name='keyImport'),
  url(r'^key/(?P<keyId>[0-9]+)/$', views.keyShow, name='keyShow'),
  url(r'^key/(?P<keyId>[0-9]+)/edit/$', views.keyEdit, name='keyEdit'),
  url(r'^key/(?P<keyId>[0-9]+)/delete/$', views.keyDelete, name='keyDelete'),
  url(r'^key/(?P<keyId>[0-9]+)/export/$', views.keyExport, name='keyExport'),
]


def breadcrumbResolve(url_name):

  from efigie.models import Key
  from django.contrib.auth.models import User
  from django.utils.text import capfirst

  key_name = Key._meta.verbose_name
  user_name = capfirst(User._meta.verbose_name)

  urls = [
    {'name': 'index', 'title': _('Home'), 'icon': 'fa-home'},
    {'name': 'about', 'title': _('About'), 'icon': 'fa-info-circle'},
    {'name': 'systemSettings', 'title': _('System Settings'), 'icon': 'fa-cog'},

    {'name': 'userLogin', 'title': _("Login"), 'icon': 'fa-sign-in'},
    {'name': 'userLogout', 'title': _("Logout"), 'icon': 'fa-sign-out'},
    {'name': 'userNew', 'title': _("New %s") % (user_name), 'icon': 'fa-plus'},
    {'name': 'userDelete', 'title': _("Delete %s") % (user_name), 'icon': 'fa-trash-o'},

    {'name': 'userNewConfirm', 'title': _("Confirmation"), 'icon': 'fa-plus'},
    {'name': 'userPasswordReset', 'title': _("Reset Password"), 'icon': 'fa-lock'},
    {'name': 'userPasswordResetConfirm', 'title': _("Confirmation"), 'icon': 'fa-lock'},

    {'name': 'userSettings', 'title': _("%s Settings") % (user_name), 'icon': 'fa-user'},
    {'name': 'userPasswordEdit', 'title': _("Edit Password"), 'icon': 'fa-lock'},
    {'name': 'userEdit', 'title': _('Edit %s') % (user_name),  'icon': 'fa-pencil'},
    {'name': 'userEditConfirm', 'title': _('Confirmation'),  'icon': 'fa-pencil'},

    {'name': 'keyList', 'title': _("%s's List") % (key_name), 'icon': 'fa-list'},
    {'name': 'keyNew', 'title': _('New %s') % (key_name), 'icon': 'fa-plus'},
    {'name': 'keyImport', 'title': _('Import %s') % (key_name), 'icon': 'fa-upload'},
    {'name': 'keyShow', 'title': _('%s') % (key_name), 'icon': 'fa-home'},
    {'name': 'keyEdit', 'title': _('Edit %s') % (key_name), 'icon': 'fa-pencil'},
    {'name': 'keyDelete', 'title': _('Delete %s') % (key_name), 'icon': 'fa-trash-o'},
    {'name': 'keyExport', 'title': _('Export %s') % (key_name), 'icon': 'fa-download'},

  ]

  for url in urls:
    if url['name'] == url_name:
      return url['title'], url['icon']

  return 'NEED TO ADD TITLE %s' % (url_name), ' '
