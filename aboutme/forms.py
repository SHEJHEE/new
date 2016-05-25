from django import forms
from .models import Content


class ContentEditForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['summary', 'work_exp', 'is_published']