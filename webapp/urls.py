from django.urls import path
from .views import home, contact , contact_details

app_name = "webapp"

urlpatterns = [
    path('', home, name='home'),
    path('<pk>/', contact_details, name='contact-details'),
    path('contact/', contact, name='contact'),
]