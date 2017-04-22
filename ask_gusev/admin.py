# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Profile, Tag, Answer, Question
from django.contrib import admin


admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Answer)
admin.site.register(Question)
