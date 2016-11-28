

from django import forms

from TV_Server import Utils

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=100,required=True)


class ManagerForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=100,required=True)
    headshot = forms.ImageField()
    nickname = forms.CharField(max_length=20)
    is_superuser = forms.BooleanField(required=False)
