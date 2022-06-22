from django import forms
from .models import todolist
class ToDoForm(forms.ModelForm):
    class Meta:
        model=todolist
        fields='__all__'