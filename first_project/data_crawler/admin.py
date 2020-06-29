from django.contrib import admin
from . import models
from .models import CategoryPaint, Paints

class CategoryPaintAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'category_name'
    ]

class PaintsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'description',
        'info',
        'wrap',
        'price',
        'info_detail'
    ]

admin.site.register(models.CategoryPaint, CategoryPaintAdmin)
admin.site.register(models.Paints, PaintsAdmin)