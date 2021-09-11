from django import forms
from .models import Contact, Response


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            "first_name",
            "last_name",
            "email",
            "reason",
            "body",
    
        )
        widgets = {
            "first_name": forms.TextInput(attrs={'class': "form-control", 'placeholder': 'first_name'}),
            "last_name": forms.TextInput(attrs={'class': "form-control", 'placeholder': 'last_name'}),
            "email": forms.TextInput(attrs={'class': "form-control", 'placeholder': 'email'}),
            "reason": forms.TextInput(attrs={'class': "form-control", 'placeholder': 'reason'}),
            "body": forms.Textarea(attrs={'class': "form-control", 'placeholder': 'body', 'style': "height: 400px"}),  
        }

class ResponseModelForm(forms.ModelForm):
    
    class Meta:
        model = Response

        fields = (
            "body",
        )
        widgets = {
            "body": forms.Textarea(attrs={'class': "form-control", 'placeholder': 'body', 'style': "height: 600px"}),
        }