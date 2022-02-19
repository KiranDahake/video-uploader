from django import forms
from .models import File
class video(forms.ModelForm):
    class Meta:
        model=File
        fields='__all__'