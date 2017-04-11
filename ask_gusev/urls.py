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
from django.conf.urls import url, include
from django.contrib import admin

from views import BaseView
from views import IndexView
from views import IndexTagView
from views import LoginView
from views import QuestionView
from views import SettingsView
from views import SignUpView
from views import AskView

urlpatterns = [
    url(r'question/', include('questions.urls')),

    url(r'^admin/', admin.site.urls),

    url(r'^base$', BaseView.as_view(), name='base'),

    url(r'^tag/blablabla$', IndexTagView.as_view(), name='tag'),

    url(r'^login$', LoginView.as_view(), name="login"),

    url(r'^question/35$', QuestionView.as_view(), name="question"),

    url(r'^settings$', SettingsView.as_view(), name="settings"),

    url(r'^signup$', SignUpView.as_view(), name="signup"),

    url(r'^ask$', AskView.as_view(), name="ask"),

    url(r'^$', IndexView.as_view(), name='index')
]
