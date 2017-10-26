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

admin.site.site_header = _('Efigie Administration')

urlpatterns = [
  url(r'^i18n/', include('django.conf.urls.i18n')),
  url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
  url(r'^admin/', admin.site.urls),

  url(r'^$', views.index, name='index'),
  url(r'^about/$', views.about, name='about'),
  url(r'^notifications/$', views.notifications, name='notifications'),
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

  url(r'^friend/$', views.friendList, name='friendList'),
  url(r'^friend/blocked/$', views.friendBlockedList, name='friendBlockedList'),
  url(r'^friend/search/$', views.friendSearch, name='friendSearch'),
  url(r'^friend/search/results/$', views.friendSearchResults, name='friendSearchResults'),
  url(r'^friend/(?P<userId>[0-9]+)/$', views.friendShow, name='friendShow'),
  url(r'^friend/(?P<userId>[0-9]+)/add/$', views.friendAdd, name='friendAdd'),
  url(r'^friend/(?P<userId>[0-9]+)/add/confirm$', views.friendAddConfirm, name='friendAddConfirm'),
  url(r'^friend/(?P<userId>[0-9]+)/cancel/$', views.friendCancel, name='friendCancel'),
  url(r'^friend/(?P<userId>[0-9]+)/block/$', views.friendBlock, name='friendBlock'),
  url(r'^friend/(?P<userId>[0-9]+)/unblock/$', views.friendUnblock, name='friendUnblock'),
  url(r'^friend/(?P<userId>[0-9]+)/delete/$', views.friendDelete, name='friendDelete'),

  url(r'^key/$', views.keyList, name='keyList'),
  url(r'^key/new/$', views.keyNew, name='keyNew'),
  url(r'^key/import/$', views.keyImport, name='keyImport'),
  url(r'^key/(?P<keyId>[0-9]+)/$', views.keyShow, name='keyShow'),
  url(r'^key/(?P<keyId>[0-9]+)/friend$', views.keyShowFriend, name='keyShowFriend'),
  url(r'^key/(?P<keyId>[0-9]+)/edit/$', views.keyEdit, name='keyEdit'),
  url(r'^key/(?P<keyId>[0-9]+)/delete/$', views.keyDelete, name='keyDelete'),
  url(r'^key/(?P<keyId>[0-9]+)/export/$', views.keyExport, name='keyExport'),

  url(r'^message/read$', views.messageRead, name='messageRead'),
  url(r'^message/set$', views.messageSet, name='messageSet'),
  url(r'^message/write$', views.messageWrite, name='messageWrite'),
  url(r'^message/settings$', views.messageSettings, name='messageSettings'),

  url(r'^image$', views.imageSearch, name='imageSearch'),
]


def breadcrumbResolve(url_name):

  from django.contrib.auth.models import User
  from django.utils.text import capfirst

  from efigie.models import Friend, Key, Message, Notification
  from efigie.utils import invariants

  key_name = Key._meta.verbose_name
  friend_name = Friend._meta.verbose_name
  message_name = Message._meta.verbose_name
  notification_name = Notification._meta.verbose_name_plural

  user_name = capfirst(User._meta.verbose_name)

  urls = [
    {'name': 'index', 'title': _('Home'), 'icon': 'fa-home'},
    {'name': 'about', 'title': _('About'), 'icon': 'fa-info-circle'},
    {'name': 'notifications', 'title': notification_name, 'icon': 'fa-bell'},

    {'name': 'systemSettings', 'title': _('System Settings'), 'icon': 'fa-cog'},

    {'name': 'userLogin', 'title': _("Login"), 'icon': 'fa-sign-in'},
    {'name': 'userLogout', 'title': _("Logout"), 'icon': 'fa-sign-out'},
    {'name': 'userNew', 'title': _("New %(model_user)s") % {'model_user': user_name}, 'icon': 'fa-plus'},
    {'name': 'userDelete', 'title': _("Delete %(model_user)s") % {'model_user': user_name}, 'icon': 'fa-trash-o'},

    {'name': 'userNewConfirm', 'title': _("Confirmation"), 'icon': 'fa-plus'},
    {'name': 'userPasswordReset', 'title': invariants.title_reset_passaword % {
      'field_password': capfirst(User._meta.get_field('password').verbose_name)}, 'icon': 'fa-lock'},
    {'name': 'userPasswordResetConfirm', 'title': _("Confirmation"), 'icon': 'fa-lock'},

    {'name': 'userSettings', 'title': _("%(model_user)s Settings") % {'model_user': user_name}, 'icon': 'fa-user'},
    {'name': 'userPasswordEdit', 'title': _("Edit %(field_password)s") % {
      'field_password': capfirst(User._meta.get_field('password').verbose_name)}, 'icon': 'fa-lock'},
    {'name': 'userEdit', 'title': _('Edit %(model_user)s') % {'model_user': user_name},  'icon': 'fa-pencil'},
    {'name': 'userEditConfirm', 'title': _('Confirmation'),  'icon': 'fa-pencil'},

    {'name': 'friendList', 'title': _("%(model_friend)s's List") % {'model_friend': friend_name}, 'icon': 'fa-list'},
    {'name': 'friendBlockedList', 'title': _("Blocked %(model_friend)s's List") % {'model_friend': friend_name}, 'icon': 'fa-ban'},
    {'name': 'friendSearch', 'title': _('Find %(model_friend)s') % {'model_friend': friend_name}, 'icon': 'fa-search'},
    {'name': 'friendSearchResults', 'title': _("%(model_friend)s's Results") % {'model_friend': friend_name}, 'icon': 'fa-address-card'},
    {'name': 'friendShow', 'title': '%(model_friend)s' % {'model_friend': friend_name}, 'icon': 'fa-user'},
    {'name': 'friendBlock', 'title': _('Block %(model_friend)s') % {'model_friend': friend_name}, 'icon': 'fa-ban'},
    {'name': 'friendDelete', 'title': _('Delete %(model_friend)s') % {'model_friend': friend_name}, 'icon': 'fa-trash-o'},

    {'name': 'keyList', 'title': _("%(model_key)s's List") % {'model_key': key_name}, 'icon': 'fa-list'},
    {'name': 'keyNew', 'title': _('New %(model_key)s') % {'model_key': key_name}, 'icon': 'fa-plus'},
    {'name': 'keyImport', 'title': _('Import %(model_key)s') % {'model_key': key_name}, 'icon': 'fa-upload'},
    {'name': 'keyShow', 'title': '%(model_key)s' % {'model_key': key_name}, 'icon': 'fa-key'},
    {'name': 'keyShowFriend', 'title': '%(model_key)s' % {'model_key': key_name}, 'icon': 'fa-key'},
    {'name': 'keyEdit', 'title': _('Edit %(model_key)s') % {'model_key': key_name}, 'icon': 'fa-pencil'},
    {'name': 'keyDelete', 'title': _('Delete %(model_key)s') % {'model_key': key_name}, 'icon': 'fa-trash-o'},
    {'name': 'keyExport', 'title': _('Export %(model_key)s') % {'model_key': key_name}, 'icon': 'fa-download'},

    {'name': 'messageWrite', 'title': _("Encrypt %(model_message)s") % {'model_message':message_name}, 'icon': 'fa-lock'},
    {'name': 'messageRead', 'title': _("Decrypt %(model_message)s") % {'model_message':message_name}, 'icon': 'fa-unlock-alt'},
    {'name': 'messageSettings', 'title': _("%(model_message)s Settings") % {'model_message':message_name}, 'icon': 'fa-comments-o'},

    {'name': 'imageSearch', 'title': _("Image Search"), 'icon': 'fa fa-google'},

  ]

  for url in urls:
    if url['name'] == url_name:
      return url['title'], url['icon']

  return 'NEED TO ADD TITLE %s' % (url_name), ' '
