from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('contacts/', views.contacts, name = 'contact'),
    path('', views.home, name = 'home')
]
