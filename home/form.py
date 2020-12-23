from django import forms
from home.models import Search



class ContactForm(forms.ModelForm):
    class Meta:
        model=Search
        fields =('Location',)