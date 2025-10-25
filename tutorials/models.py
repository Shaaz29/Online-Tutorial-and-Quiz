from django.db import models 

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    reference_link = models.URLField(blank=True, null=True, help_text="Optional: Add a GFG or YouTube link for this tutorial.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name='tutorials', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# 👇 New models for Quiz System

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name="quizzes", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name="questions", on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text


class Option(models.Model):
    question = models.ForeignKey(Question, related_name="options", on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)
    explanation_link = models.URLField(blank=True, null=True)  # 👈 Add hyperlink for explanation

    def __str__(self):
        return self.text
