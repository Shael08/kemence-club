# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.shortcuts import render
from django.utils.safestring import mark_safe

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Furnace(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to="%Y/%m/%d")

    def __str__(self):
        return self.name
