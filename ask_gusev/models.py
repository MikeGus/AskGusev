# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Count, Sum


class Profile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='uploads')
    info = models.TextField()


class TagManager(models.Manager):
    def count_questions(self):
        return self.annotate(questions_count=Count('question'))

    def order_by_count(self):
        return self.count_questions().order_by(-'questions_count')

    def get_by_title(self, title):
        return self.get(title='title')

    def get_or_create(self, title):
        try:
            tag = self.get_by_title(title)
        except Tag.DoesNotExist:
            tag = self.create(title=title)
        return tag

    def count_popular(self):
        questions_count = Count('question')

        return self.order_by_count().all()[:10]


class Tag(models.Model):
    title = models.CharField(max_length = 15)

    objects = TagManager()

    def get_url(self):
        return '/tag/' + self.title


class QuestionManager(models.Manager):

    def new(self):
        return self.order_by('-date')

    def hot(self):
        return self.order_by('-rating')

    def tag(self, tag):
        return self.filter(tags=tag)


class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey(User)
    date = models.DateTimeField()
    tags = models.ManyToManyField(Tag)
    rating = models.IntegerField(default=0)

    objects = QuestionManager()

    class Meta:
        db_table = 'questions'
        ordering = ['-date']

    def get_answers(self):
        return Answer.objects.filter(question_id=self.id)


class QuestionLikeManager(models.Manager):

    def calculate(self, question):
        return self.filter(question=question).aggregate(sum=Sum('value'))['sum']

    def update(self, author, question, value):
        obj, new = self.update_or_create(
            author=author,
            question=question,
            defaults={'value': value}
        )

        question.rating = self.calculate(question)
        question.save()

        return new


class QuestionRating(models.Model):
    PLUS = 1
    MINUS = -1

    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
    value = models.SmallIntegerField(default=1)

    objects = QuestionLikeManager()


class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
    date = models.DateTimeField(default=timezone.now)
    correct = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)

    class Meta:
        db_table = 'answer'
        ordering = ['-correct', 'date', '-rating']

    def get_url(self):
        return self.question.get_url()


class AnswerRatingManager(models.Manager):
    def calculate(self, answer):
        return self.filter(answer=answer).aggregate(sum=Sum('value'))['sum']

    def update(self, author, answer, value):
        obj, new = self.update(
            author=author,
            answer=answer,
            defaults={'value':value}
        )

        answer.rating = self.calculate(answer)
        answer.save()

        return new


class AnswerRating(models.Model):
    PLUS = 1
    MINUS = -1

    answer = models.ForeignKey(Answer)
    author = models.ForeignKey(User)
    value = models.SmallIntegerField(default=1)

    objects = AnswerRatingManager()
