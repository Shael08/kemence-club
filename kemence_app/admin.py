# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Post, Furnace

# Register your models here.

admin.site.register(Post)


class FurnaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

admin.site.register(Furnace, FurnaceAdmin)

#admin.site.register(FurnaceImg)
