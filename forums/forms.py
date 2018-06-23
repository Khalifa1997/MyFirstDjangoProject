from django import forms
from .models import board, reply,thread

class NewThreadForm(forms.ModelForm):

    class meta:
        model=thread
        fields= ['title','body']

class NewReplyForm(forms.ModelForm):
    class meta:
        model=reply
        fields= ['text']