# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from collections import namedtuple
import models


def get_page(request):
    page = request.GET.get('page')
    if page is None or not page.isdigit():
        page = 1
    else:
        page = int(page)

    return page


def pagination(request, object_list, per_page=1, page=1):

    max_page = len(object_list.questions) // per_page
    if len(object_list.questions) % per_page != 0:
        max_page += 1

    if page > max_page:
        current_page = 1
        if per_page > len(object_list.questions):
            questions_to_render = object_list.questions
        else:
            questions_to_render = object_list.questions[:per_page]
    else:
        current_page = page
        questions_to_render = object_list.questions[per_page * (page - 1): per_page * (page)]

    next_page = current_page + 1
    prev_page = current_page - 1

    prev_max_page = max_page - 1
    prev_prev_max_page = prev_max_page - 1

    if current_page == 1:
        prev_page = 1
    if per_page * current_page >= len(object_list.questions):
        next_page = current_page
    context = {'questions' : questions_to_render, 'current_page' : current_page,
               'next_page' : next_page, 'prev_page' : prev_page, 'max_page' : max_page,
               'prev_max_page' : prev_max_page, 'prev_prev_max_page' : prev_prev_max_page,
               'tag' : object_list.tag, 'hot' : object_list.hot}
    return render(request, object_list.template, context)


def index(request):

    object_list = namedtuple('hot', 'tag', 'questions', 'template')

    page = get_page(request)

    object_list.questions = models.Question.objects.all()
    object_list.template = "index.html"
    object_list.tag = None
    object_list.hot = False

    return pagination(request, object_list, page=page)


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


# def question(request, question_id):
#
#     q = {
#             "title": "title " + str(question_id),
#             "id": question_id,
#             "text": "text " + str(question_id),
#             "tags": ["bender", "frei"],
#             "rating": question_id,
#             "hot" : int(question_id) % 2,
#             "answers": int(question_id) % 5
#         }
#     answers = []
#     for i in range (int(question_id) % 5):
#         answers.append({
#             "title": "answer " + str(i),
#             "id": i,
#             "text": "text " + str(i),
#             "rating": i,
#         })
#
#     return render(request, "question.html", {"object": q, "answers": answers})


def settings(request):
    return render(request, "settings.html")


def ask(request):
    return render(request, "ask.html")


def tag(request, tag_title):
    tag_id = models.Tag.objects.get_by_title(tag_title).id
    object_list = namedtuple('hot', 'tag', 'questions', 'template')
    object_list.hot = False
    object_list.questions = models.Question.objects.tag(tag_id)
    object_list.template = "index.html"
    object_list.tag = tag_title
    return pagination(request, object_list)


def hot(request):
    object_list = namedtuple('hot', 'tag', 'questions', 'template')
    object_list.hot = True
    object_list.tag = None
    object_list.template = "index.html"
    object_list.questions = models.Question.objects.hot()
    page = request.GET.get('page')
    if page is None or not page.isdigit():
        page = 1
    else:
        page = int(page)

    return pagination(request, object_list, page=page)


def question(request, question_id):
    question = models.Question.objects.get(id=question_id)
    answers = question.get_answers()

    return render(request, "question.html", {"object": question, "answers": answers})