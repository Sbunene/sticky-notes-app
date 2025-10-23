# notes/forms.py
from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    """Form to create and edit Note objects."""
    class Meta:
        model = Note
        fields = ["title", "content"]