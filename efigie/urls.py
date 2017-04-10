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




  # url(r'^criar-conta/$', efigie.views.register, name='register'),
  # url(r'^nova-senha/$', efigie.views.password_reset, name='password_reset'),
  # url(r'^$', efigie.views.index, name='index'),
  # url(r'^admin/', admin.site.urls),
]
