from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
  birthday = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd ex. 1995-01-30'}))
  class Meta:
    model = Profile
    exclude = ['user']
