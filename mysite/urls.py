"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
#from django.conf.urls import url
from django.urls import re_path

from django.contrib import admin

from views import hello, insert, json_1, json_y, json_r, start, stop, points, plot

admin.autodiscover()

urlpatterns = [
    re_path(r'^$', hello),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^json/$', json_1),
    re_path(r'^json_y/$', json_y),
    re_path(r'^json_r/$', json_r),
    re_path(r'^insert/$', insert),
    re_path(r'^start/$', start),
    re_path(r'^stop/$', stop),
    re_path(r'^json_p/$', points),
    re_path(r'^json_plot/$', plot),
]