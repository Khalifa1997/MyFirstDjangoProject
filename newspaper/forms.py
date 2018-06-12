from django import forms
from .models import article, comment

class NewArticleForm(forms.ModelForm):
    #comments = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = article
        fields = ['title', 'body']

class NewCommentForm(forms.ModelForm):
    #comments = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = comment
        fields = ['text']