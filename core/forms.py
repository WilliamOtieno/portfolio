from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    model = Contact
    fields = [
        "name",
        "email",
        "subject",
        "message"
    ]
