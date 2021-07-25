from django.urls import path
from .views import home, contact

app_name = "webapp"

urlpatterns = [
    path('home/', home, name='home'),
    path('contact/', contact, name='contact'),
]