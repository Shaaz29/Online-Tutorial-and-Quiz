from django.contrib import admin
from .models import Quiz, Question, QuizResult

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    fields = ['question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer']

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by', 'created_at']
    list_filter = ['created_by', 'created_at']
    search_fields = ['title', 'description']
    inlines = [QuestionInline]
    date_hierarchy = 'created_at'

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'quiz', 'correct_answer']
    list_filter = ['quiz']
    search_fields = ['question_text']

@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ['user', 'quiz', 'score', 'taken_at']
    list_filter = ['quiz', 'taken_at']
    search_fields = ['user__username', 'quiz__title']
    date_hierarchy = 'taken_at'