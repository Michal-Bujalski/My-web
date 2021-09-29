from django.shortcuts import render, redirect
from .models import Contact, Response
from .froms import ContactModelForm, ResponseModelForm

def home(request):
    return render(request, "webapp/home.html", {})

def contact_list(request):
    forms = Contact.objects.all()
    context = {
        "forms": forms
    }
    return render(request, "webapp/contact_list.html", context)

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
            return redirect("webapp:contact_list")
    context = {
        "form": form
    }
    return render(request, "webapp/contact.html", context)

# It is important to name our secend argument pk becouse django know it is primary key from Contact model.
def contact_details(request, pk):
    form = Contact.objects.get(id=pk)
    context = {
        "form": form
    }
    return render(request, "webapp/contact_details.html", context)

def contact_delete(request, pk):
    contact = Contact.objects.get(id=pk)
    contact.delete()
    return redirect("webapp:contact_list")

def resume(request):
    return render(request, "webapp/resume.html", {})


def my_response(request, pk):
    form = Contact.objects.get(id=pk)

    if form.my_response:
        body = Response.objects.all()
        context = {
            "form": form,
            "body": body
        }
        return render(request, "webapp/my_response.html", context)
    else:

        form2 = ResponseModelForm()
        context = {
            "form2": form2
        }
        if request.method == "POST":
            form2 = ResponseModelForm(request.POST)
            if form2.is_valid():
                Contact.objects.filter(pk=pk).update(my_response=True)

                form2.contact = form
                body = form2.cleaned_data["body"]
                Response.objects.create(
                    contact=form,
                    body=body
                )
                return redirect("webapp:contact_list")

        return render(request, "webapp/response.html", context)
        