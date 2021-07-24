from django.shortcuts import render
from .models import Contact
from .froms import ContactForm

# Create your views here.
def index(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print("The form is valid")
            print(form.cleaned_data)
            first_name = forms.cleaned_data["first_name"]
            last_name = forms.cleaned_data["last_name)"]
            email = forms.EmailField["email"]
            contact = forms.cleaned_data["contact"]
            body = forms.cleaned_data["body"]
            Contact.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                contact=contact,
                body=body,
            )
            print("Contact user created")
    context = {
        "form": form
    }
    return render(request, 'index.html', context)
