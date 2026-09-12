from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('contacts/', views.contacts, name = 'contact'),
    path('home/', views.home, name = 'home'),
    path('details/<int:id_product>', views.details, name = 'details'),
]
