from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Link(models.Model):
    link_text = models.CharField(max_length=255)
    link_img = models.ImageField(upload_to='img/', null=True)
    pub_date = models.DateTimeField('date published')


class News(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    text = models.CharField(max_length=5000)
    img = models.ImageField(upload_to='img/', null=True)
    video_url = models.CharField(max_length=5000)


class Photo(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photo/', null=True)


class Message(models.Model):
    chat = models.ForeignKey(
        Link,
        verbose_name='Чат под новостью',
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        verbose_name='Пользователь', on_delete=models.CASCADE)
    message = models.TextField('Сообщение')
    pub_date = models.DateTimeField(
        'Дата сообщения',
        default=timezone.now)


class Mark(models.Model):
    riddle = models.ForeignKey(
        Link,
        verbose_name='Загадка',
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        verbose_name='Пользователь', on_delete=models.CASCADE)
    mark = models.IntegerField(
        verbose_name='Оценка')
    pub_date = models.DateTimeField(
        'Дата оценки',
        default=timezone.now)
