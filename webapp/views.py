from django.shortcuts import render, redirect
from .models import Contact
from .froms import ContactModelForm

def home(request):
    forms = Contact.objects.all()
    context = {
        "forms": forms
    }
    return render(request, "webapp/home.html", context)


def contact(request):
    form = ContactModelForm()
    if request.method == "POST":
        form = ContactModelForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            reason = form.cleaned_data["reason"]
            body = form.cleaned_data["body"]
            Contact.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                reason=reason,
                body=body,
            )
            # Return redirect to home page prom django sortcuts 
            return render(request, "webapp/home.html")
    context = {
        "form": form
    }
    return render(request, 'webapp/contact.html', context)

# It is important to name our secend argument pk becouse django know it is primary key from Contact model.
def contact_details(request, pk):
    form = Contact.objects.get(id=pk)
    context = {
        "form": form
    }
    return render(request, 'webapp/contact-details.html', context)