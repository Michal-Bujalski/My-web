from django.shortcuts import render
from .models import Contact
from .froms import ContactForm, ContactModelForm

def home(request):
    forms = Contact.objects.all()
    print(forms)
    context = {
        "forms": forms
    }
    return render(request, "home.html", context)


def contact(request):
    form = ContactModelForm()
    if request.method == "POST":
        form = ContactModelForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            # Need update views with reasen model and fix contact field
            email = form.cleaned_data["email"]
            contact = form.cleaned_data["contact"]
            body = form.cleaned_data["body"]
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
    return render(request, 'contact.html', context)

# def contact(request):
#     form = ContactForm()
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             print("The form is valid")
#             print(form.cleaned_data)
#             first_name = form.cleaned_data["first_name"]
#             last_name = form.cleaned_data["last_name"]
#             email = form.cleaned_data["email"]
#             contact = form.cleaned_data["contact"]
#             body = form.cleaned_data["body"]
#             Contact.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 email=email,
#                 contact=contact,
#                 body=body,
#             )
#             print("Contact user created")
#     context = {
#         "form": form
#     }
#     return render(request, 'contact.html', context)
