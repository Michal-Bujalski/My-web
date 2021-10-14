from django.urls import path
from .views import home, contact, contact_list, contact_details, contact_delete, resume, my_response

app_name = "webapp"

urlpatterns = [
    path('', home, name='home'),
    path('contact/list', contact_list, name='contact_list'),
    path('<int:pk>/', contact_details, name='contact_details'),
    path('<int:pk>/delete/', contact_delete, name='contact_delete'),
    path('<int:pk>/my_response/', my_response, name='my_response'),
    path('<int:pk>/response/', my_response, name='response'),
    path('contact/', contact, name='contact'),
    path('resume/', resume, name='resume'),
]
