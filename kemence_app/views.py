# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils import timezone
from .models import Post, Furnace

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'kemence_app/post_list.html', {'posts': posts})

def furnace_list(request):
    furnaces = Furnace.objects.all()
    return render(request, 'kemence_app/furnace_list.html', {'furnaces': furnaces})
