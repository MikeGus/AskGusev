"""ask_gusev URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/?', views.login, name="login"),
    #url(r'^tag/(?P<tag_id>[a-z]+)/$', views.index, name="tag"),
    #url(r'^hot/$', views.index, {'hot':True}, name="hot"),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.question, name="question"),
    url(r'^settings/?', views.settings, name="settings"),
    url(r'^signup/?', views.signup, name="signup"),
    url(r'^ask/?', views.ask, name="ask"),
    url(r'^$', views.index, name='index'),

    url(r'^tag/(?P<tag_title>.+)/$', views.tag, name="tag"),
    url(r'^hot/$', views.hot, name="hot"),
]
