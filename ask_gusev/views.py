# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render


def index(request):
    questions = []
    for i in xrange(1, 10):
        questions.append({
            "title" : "title "  + str(i),
            "id" : i,
            "text" : "text " + str(i),
            "tags" : {"bender", "frei"},
            "rating" : i,
        })
    context = {'questions' : questions,}
    return render(request, "index.html", context);


def login(request):
    return render(request, "login.html");


def signup(request):
    return render(request, "signup.html");


def question(request):
    return render(request, "question.html");


def settings(request):
    return render(request, "settings.html");


def ask(request):
    return render(request, "ask.html");
