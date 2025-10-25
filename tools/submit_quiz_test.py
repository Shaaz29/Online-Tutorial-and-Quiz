import os
import sys
import django
import traceback

# Prepare Django
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_tutorial_system.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.test import Client
from quizzes.models import Quiz

User = get_user_model()
# Create or get a test user
user, created = User.objects.get_or_create(username='autotest')
if created:
    user.set_password('pass1234')
    user.save()
    print('Created test user: autotest / pass1234')
else:
    print('Test user exists: autotest')

c = Client()
logged = c.login(username='autotest', password='pass1234')
print('Logged in:', logged)

try:
    quiz = Quiz.objects.first()
    if not quiz:
        print('No quizzes found in database. Abort.')
        sys.exit(0)
    print('Using quiz:', quiz.id, quiz.title)

    post_data = {}
    for q in quiz.questions.all():
        # choose option_a as a default answer
        post_data[f'question_{q.id}'] = getattr(q, 'option_a', '')
    print('Posting answers for questions:', list(post_data.keys()))

    # include HTTP_HOST to avoid DisallowedHost when using the test client
    response = c.post(f'/quizzes/{quiz.id}/submit/', post_data, HTTP_HOST='127.0.0.1')
    print('Response status code:', response.status_code)
    content = response.content.decode(errors='replace')
    print('Response content (first 2000 chars):')
    print(content[:2000])
except Exception:
    traceback.print_exc()
