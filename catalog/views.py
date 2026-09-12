from django.shortcuts import render


def contacts(requests):
    return render(requests, 'catalog/contacts.html')


def home(requests):
    return render(requests, 'catalog/home.html')

def example(requests):
    return render(requests, 'catalog/example.html')
