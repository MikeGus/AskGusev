from django.conf.urls import url

from questions.views import AboutView
from questions.views import get_post

urlpatterns = [
    url(r'^about', AboutView.as_view(), name='about'),
    url(r'^post$', get_post, name='getpost'),
]
