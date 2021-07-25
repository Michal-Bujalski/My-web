from django import forms
from .models import Contact

class ContactForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    contact = forms.CharField()
    body = forms.CharField()

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            "first_name",
            "last_name",
            "email",
            "contact",
            "body",
    
        )
        widget = {
            "first_name": forms.TextInput(attrs={'class': "form-control"}),
            "last_name": forms.TextInput(attrs={'class': "form-control"}),
            "email": forms.TextInput(attrs={'class': "form-control"}),
            "contact": forms.TextInput(attrs={'class': "form-control"}),
            "body": forms.Textarea(attrs={'class': "form-control"}),  
        }