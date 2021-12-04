from django.shortcuts import render

from web.models import About, Address, Category, Contact, Gallery


def index(request):
    categories = Category.objects.all()
    galleries = Gallery.objects.all()
    contacts = Contact.objects.all()
    abouts = About.objects.get()
    addresses = Address.objects.all()

    context = {
        "categories" : categories,
        "galleries" : galleries,
        "contacts" : contacts,
        "abouts" : abouts,
        "addresses" : addresses,
    }

    return render(request,"index.html",context=context)