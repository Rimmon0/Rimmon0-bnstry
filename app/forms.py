"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from.models import Comment
from.models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))
class CommentForm (forms.ModelForm):
   class Meta:
     model = Comment                        # используемая модель
     fields = ('text',)                     # требуется заполнить только поле text
     labels = {'text': "Комментарий"}       # метка к полю формы text

class BlogForm (forms.ModelForm):
   class Meta:
     model = Blog                                               # используемая модель
     fields = ('title','description','image','content')         # ввод заголовка, краткого содержания, выбора файла картинки и полного содержания статьи
     labels = {'title': 
               "Заголовок", 'description': 
               "Краткое содержание", 'image': 
               "Путь к картинке", 'content': 
               "Полное содержание"} # метка к полю формы text
 