from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Quiz, Question, QuizResult
import traceback
import os
from datetime import datetime

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes/quiz_list.html', {'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    user_rank = None
    if request.user.is_authenticated:
        results = QuizResult.objects.filter(quiz=quiz).order_by('-score', 'taken_at')
        user_result = results.filter(user=request.user).order_by('-taken_at').first()
        if user_result:
            unique_scores = list(results.values_list('score', flat=True).distinct())
            unique_scores.sort(reverse=True)
            user_rank = unique_scores.index(user_result.score) + 1
    return render(request, 'quizzes/quiz_detail.html', {'quiz': quiz, 'user_rank': user_rank})

@login_required
def submit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == 'POST':
        try:
            score = 0
            total_questions = quiz.questions.count()
            responses = {}
            for question in quiz.questions.all():
                selected_answer = request.POST.get(f'question_{question.id}')
                responses[str(question.id)] = selected_answer
                if selected_answer and selected_answer == question.correct_answer:
                    score += 1

            user_result = QuizResult.objects.create(
                user=request.user,
                quiz=quiz,
                score=score,
                responses=responses
            )

            results = QuizResult.objects.filter(quiz=quiz).order_by('-score', 'taken_at')
            unique_scores = list(results.values_list('score', flat=True).distinct())
            unique_scores.sort(reverse=True)
            user_rank = unique_scores.index(user_result.score) + 1 if user_result.score in unique_scores else 0

            if user_rank and user_rank <= 10:
                rank_comment = "Excellent"
            elif user_rank and user_rank <= 30:
                rank_comment = "Very Good"
            elif user_rank and user_rank <= 50:
                rank_comment = "Good"
            else:
                rank_comment = "Keep Practicing"

            return render(request, 'quizzes/quiz_result.html', {
                'quiz': quiz,
                'score': score,
                'total_questions': total_questions,
                'percent': int((score / total_questions) * 100) if total_questions > 0 else 0,
                'user_rank': user_rank,
                'rank_comment': rank_comment,
                'responses': responses,
                'show_references': True
            })
        except Exception as e:
            tb = traceback.format_exc()
            print(f"Error submitting quiz {quiz_id}: {e}\n{tb}")
            messages.error(request, "An error occurred while submitting your quiz.")
            return redirect('quizzes:quiz_detail', quiz_id=quiz_id)
    return redirect('quizzes:quiz_detail', quiz_id=quiz_id)
