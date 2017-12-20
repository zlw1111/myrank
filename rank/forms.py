# -*- coding: utf-8 -*-

from django import forms
from .models import Comment,Myself

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['des']

class MyselfCreateForm(forms.ModelForm):
    class Meta:
        model = Myself
        fields = ['name', 'psw']
