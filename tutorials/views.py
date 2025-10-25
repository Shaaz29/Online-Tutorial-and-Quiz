from django.shortcuts import render, get_object_or_404
from .models import Quiz, Tutorial

def tutorial_list(request):
    tutorials = Tutorial.objects.all().order_by('-created_at')
    return render(request, 'tutorials/tutorial_list.html', {'tutorials': tutorials})


def tutorial_detail(request, tutorial_id):
    tutorial = get_object_or_404(Tutorial, id=tutorial_id)
    return render(request, 'tutorials/tutorial_detail.html', {'tutorial': tutorial})


def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    # Use the existing quizzes template for taking quizzes
    return render(request, "quizzes/quiz_detail.html", {"quiz": quiz, "questions": questions})
