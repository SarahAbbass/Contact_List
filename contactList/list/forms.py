from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'address', 'profession1', 'profession2', 'email', 'tel_number', 'date_added']
