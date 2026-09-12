from django.shortcuts import render
from .models import Product


def contacts(request):
    return render(request, 'catalog/contacts.html')


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/home.html', context)


def details(request, id_product):
    product = Product.objects.get(id=id_product)
    context = {'product': product}
    return render(request, 'catalog/details.html', context)
