from django import forms
from .models import signup

class signupModel(forms.ModelForm):
    class Meta:
        model=signup
        fields='__all__'