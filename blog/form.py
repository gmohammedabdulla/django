from django import forms

from .models import Latlag

class PostForm(forms.ModelForm):

    class Meta:
        model = Latlag
        fields = ('lat', 'lag')