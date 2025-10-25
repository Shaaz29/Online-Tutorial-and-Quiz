from django.contrib import admin
from .models import Category, Tutorial, Quiz, Question, Option


# Inline Options inside Question (so you can add them on same page)
class OptionInline(admin.TabularInline):
    model = Option
    extra = 2   # shows 2 empty option fields by default


# Inline Questions inside Quiz
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


# Admin for Quiz
class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


# Admin for Question (with options inline)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]


# Register models
admin.site.register(Category)
admin.site.register(Tutorial)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option)
