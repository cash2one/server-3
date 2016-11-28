from django import forms

from Serials.models import Serials


class VideoAddForm(forms.Form):
    title = forms.CharField(required=True)
    describe = forms.CharField(required=True)
    video_url = forms.FileField()
    serials = forms.ModelChoiceField(queryset=Serials.objects.all())

