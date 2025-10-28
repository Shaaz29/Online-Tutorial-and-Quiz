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
            # Record submission attempt for debugging: timestamp, user, quiz, and posted keys
            try:
                submissions_dir = os.path.join(os.getcwd(), 'logs')
                os.makedirs(submissions_dir, exist_ok=True)
                submissions_log = os.path.join(submissions_dir, 'quiz_submissions.log')
                with open(submissions_log, 'a', encoding='utf-8') as sf:
                    sf.write(f"[{datetime.utcnow().isoformat()}] user={getattr(request.user, 'username', 'anonymous')} quiz_id={quiz_id} POST_keys={list(request.POST.keys())}\n")
            except Exception as _log_exc:
                print('Failed to write quiz submission trace:', _log_exc)

            score = 0
            total_questions = quiz.questions.count()
            responses = {}
            for question in quiz.questions.all():
                # programmatic form.submit() may bypass HTML validation, so default to None
                selected_answer = request.POST.get(f'question_{question.id}')
                responses[str(question.id)] = selected_answer
                if selected_answer is not None and selected_answer == question.correct_answer:
                    score += 1

            # Save quiz result with responses
            user_result = QuizResult.objects.create(
                user=request.user,
                quiz=quiz,
                score=score,
                responses=responses
            )

            # Calculate rank
            results = QuizResult.objects.filter(quiz=quiz).order_by('-score', 'taken_at')
            unique_scores = list(results.values_list('score', flat=True).distinct())
            unique_scores.sort(reverse=True)
            user_rank = unique_scores.index(user_result.score) + 1 if user_result.score in unique_scores else 0

            # Add comment based on rank
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
            # Log the error to the server console for debugging and show a user-friendly message
            tb = traceback.format_exc()
            print(f"Error submitting quiz {quiz_id} by user {request.user}: {e}\n{tb}")
            # Ensure logs directory exists and append the traceback for post-mortem
            try:
                logs_dir = os.path.join(os.getcwd(), 'logs')
                os.makedirs(logs_dir, exist_ok=True)
                log_path = os.path.join(logs_dir, 'quiz_errors.log')
                with open(log_path, 'a', encoding='utf-8') as f:
                    f.write(f"[{datetime.utcnow().isoformat()}] Error submitting quiz {quiz_id} by user {request.user}\n")
                    f.write(tb)
                    f.write('\n' + ('-'*80) + '\n')
            except Exception as log_exc:
                print('Failed to write quiz error log:', log_exc)
            messages.error(request, "An error occurred while submitting your quiz. Please try again.")
            return redirect('quizzes:quiz_detail', quiz_id=quiz_id)
    return redirect('quizzes:quiz_detail', quiz_id=quiz_id)
