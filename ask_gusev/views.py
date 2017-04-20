# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from collections import namedtuple


def pagination(request, object_list):
    if (object_list.per_page * object_list.page) > len(object_list.questions):
        current_page = 1
        if object_list.per_page > len(object_list.questions):
            questions_to_render = object_list.questions
        else:
            questions_to_render = object_list.questions[:object_list.per_page]
    else:
        current_page = object_list.page
        questions_to_render = object_list.questions[object_list.per_page * (object_list.page - 1): object_list.per_page * (object_list.page)]

    next_page = current_page + 1
    prev_page = current_page - 1

    max_page = len(object_list.questions) // object_list.per_page
    if len(object_list.questions) % object_list.per_page != 0:
        max_page += 1
    prev_max_page = max_page - 1
    prev_prev_max_page = prev_max_page - 1

    if current_page == 1:
        prev_page = 1
    if object_list.per_page * current_page >= len(object_list.questions):
        next_page = current_page
    context = {'questions' : questions_to_render, 'current_page' : current_page,
               'next_page' : next_page, 'prev_page' : prev_page, 'max_page' : max_page,
               'prev_max_page' : prev_max_page, 'prev_prev_max_page' : prev_prev_max_page}
    return render(request, object_list.template, context)


def index(request):
    questions = []
    for i in xrange(1, 120):
        questions.append({
            "title" : "title "  + str(i),
            "id" : i,
            "text" : "text " + str(i),
            "tags" : {"bender", "frei"},
            "rating" : i,
        })

    object_list = namedtuple('pagination_data', ['per_page', 'page', 'questions', 'template'])
    object_list.per_page = 10
    object_list.page = 5
    object_list.questions = questions
    object_list.template = "index.html"

    return pagination(request, object_list)


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


def question(request):
    return render(request, "question.html")


def settings(request):
    return render(request, "settings.html")


def ask(request):
    return render(request, "ask.html")
