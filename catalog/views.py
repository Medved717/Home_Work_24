from django.shortcuts import render
from .models import Product


def contacts(requests):
    return render(requests, 'catalog/contacts.html')


def home(requests):
    products = Product.objects.all()
    context = {'products': products}
    return render(requests, 'catalog/home.html', context)
