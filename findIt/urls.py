"""findIt URL Configuration

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
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView, TemplateView

from item.urls import (
  house as house_urls)
from user import urls as user_urls

admin.site.site_header = 'Find It Admin'
admin.site.site_title = 'Find It Site Admin'

urlpatterns = [
  url(r'^$', RedirectView.as_view(
      pattern_name='dj-auth:login',
      permanent=False)),
  url(r'^admin/', admin.site.urls),
  url(r'^about/$', TemplateView.as_view(
    template_name='site/about.html'),
    name='about_site'),
  url(r'^user/', include(
    user_urls,
    app_name='user',
    namespace='dj-auth')),
  url(r'^house/', include(house_urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
