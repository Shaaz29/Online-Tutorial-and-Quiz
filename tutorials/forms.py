from django import forms
from .models import Tutorial

class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ['title', 'description', 'content', 'category']  # Adjust fields as per your model
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
            'content': forms.Textarea(attrs={'rows': 10, 'cols': 30}),
        }