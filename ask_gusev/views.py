# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from collections import namedtuple
import models


def pagination(request, object_list, per_page=10, page=1):

    max_page = len(object_list.questions) // per_page
    if len(object_list.questions) % per_page != 0:
        max_page += 1

    if object_list.page > max_page:
        current_page = 1
        if per_page > len(object_list.questions):
            questions_to_render = object_list.questions
        else:
            questions_to_render = object_list.questions[:per_page]
    else:
        current_page = object_list.page
        questions_to_render = object_list.questions[per_page * (object_list.page - 1): per_page * (object_list.page)]

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


def index(request, tag_id=None, hot=False):

    questions = []
    for i in xrange(1, 122):
        questions.append({
            "title": "title " + str(i),
            "id": i,
            "text": "text " + str(i),
            "tags": ["bender", "frei"],
            "rating": i % 15,
            "answers": i % 5
        })

    object_list = namedtuple('pagination_data', ['per_page', 'page', 'questions', 'template'])

    page = request.GET.get('page')
    if page is None or not page.isdigit():
        page = 1
    else:
        page = int(page)

    object_list.page = page
    object_list.template = "index.html"

    object_list.tag = tag_id
    object_list.questions = []
    object_list.hot = hot

    if object_list.tag is None:
        if not hot:
            object_list.questions = questions
        else:
            for q in questions:
                if q['rating'] > 8:
                    object_list.questions.append(q)
    else:
        for q in questions:
            if object_list.tag in q['tags']:
                object_list.questions.append(q)

    return pagination(request, object_list, page=page)


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


def question(request, question_id):

    q = {
            "title": "title " + str(question_id),
            "id": question_id,
            "text": "text " + str(question_id),
            "tags": ["bender", "frei"],
            "rating": question_id,
            "hot" : int(question_id) % 2,
            "answers": int(question_id) % 5
        }
    answers = []
    for i in range (int(question_id) % 5):
        answers.append({
            "title": "answer " + str(i),
            "id": i,
            "text": "text " + str(i),
            "rating": i,
        })

    return render(request, "question.html", {"object": q, "answers": answers})


def settings(request):
    return render(request, "settings.html")


def ask(request):
    return render(request, "ask.html")
#
#
# def tag(request, tag):
#     return pagination(request, {models.Question.objects.tag(tag), 1, False, "index.html"})
#
#
# def hot(request):
#
#
# def question(request, question_id):
#     question = models.Question.objects.get(id=question_id)
#     answers = question.get_answers()
#
#     return render(request, "question.html", {"object": question, "answers": answers})