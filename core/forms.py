from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea, required=True)
