from django.shortcuts import render
from .models import Contact

# Create your views here.
def index(request):
    contact = Contact.objects.all()
    context = {
        "contact": contact
    }
    return render(request, 'index.html', context)
