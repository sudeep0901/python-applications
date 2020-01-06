from django import forms
from django.forms import ValidationError

from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

    def clean_email(self):
        print("performing validation of email")
        email = self.cleaned_data['email']

        if not email.endswith('@gmail.com'):
            raise ValidationError('Domain of email is not valid')
        return email


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ('name', 'email', 'body')



class SearchForm(forms.Form):
    query = forms.CharField()
