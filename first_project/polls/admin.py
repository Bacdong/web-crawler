from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    # fields = [
    #     'pub-date',
    #     'question_text'
    # ]
    fieldset = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub-date']}),
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
