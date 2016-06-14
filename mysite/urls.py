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
from django.conf.urls import url
from django.contrib import admin

from views import hello, insert, json_1, json_y, json_r, start, stop, points, plot

admin.autodiscover()

urlpatterns = [
    url(r'^$', hello),
    url(r'^admin/', admin.site.urls),
    url(r'^json/$', json_1),
    url(r'^json_y/$', json_y),
    url(r'^json_r/$', json_r),
    url(r'^insert/$', insert),
    url(r'^start/$', start),
    url(r'^stop/$', stop),
    url(r'^json_p/$', points),
    url(r'^json_plot/$', plot),
]