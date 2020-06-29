from django.contrib import admin
from . import models
from .models import Article, Reporter

class ReporterAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'fullName',
    ]

    list_filter = ['id']
    search_fields = ['fullName']

class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'headLine',
        'content',
        'reporter_id',
        'pub_date',
    ]

admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Reporter, ReporterAdmin)