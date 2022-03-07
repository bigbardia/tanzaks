from django import forms
from meme.models import Meme


class MemeForm(forms.ModelForm):

    class Meta:
        model = Meme
        fields = ["image","title"]
