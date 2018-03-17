# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Article
from django.contrib import admin
from .models import Person


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'update_time',)
    search_fields = ('title', 'pub_date')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    search_fields = ('first_name',)


class MyModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(MyModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=request.user)
        

admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)
