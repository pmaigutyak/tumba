from django import forms
from .models import Tumb

class TumbForm(forms.ModelForm):
    class Meta:
        model = Tumb
        fields = ['name', 'price', 'description']