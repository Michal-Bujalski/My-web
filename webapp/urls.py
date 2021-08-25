from django.urls import path
from .views import home, contact , contact_details, contact_delete, resume

app_name = "webapp"

urlpatterns = [
    path('', home, name='home'),
    path('<int:pk>/', contact_details, name='contact_details'),
    path('<int:pk>/delete/', contact_delete, name='contact_delete'),
    path('contact/', contact, name='contact'),
    path('resume/', resume, name='resume'),
]