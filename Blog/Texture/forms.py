from django import forms
from .models import Category, Textures
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class TextureForm(forms.ModelForm):

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValueError('Заголовок не должен начинаться с цифр')
        return title

    class Meta:
        model = Textures
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
                }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
                }),
            'category': forms.Select(attrs={
                'class': 'form-control'
                }),
          }
