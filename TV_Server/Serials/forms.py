from django import forms

from Tags.models import Tag


class SerialsForm(forms.Form):
    catagory = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
    type = forms.CharField(max_length=1,required=True)
    headshot = forms.ImageField()
    title = forms.CharField(max_length=20)
    describe = forms.CharField(max_length=500)
    director = forms.CharField(max_length=20)
    actors = forms.CharField(max_length=100)