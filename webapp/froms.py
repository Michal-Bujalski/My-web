from django import forms
from .models import Contact

# class ContactForm(forms.Form):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     email = forms.EmailField()
#     reason = forms.CharField()
#     body = forms.CharField()

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