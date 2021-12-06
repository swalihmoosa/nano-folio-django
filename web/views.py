from django.shortcuts import render

from web.models import About, Address, Category, Contact, Gallery
from web.forms import ContactForm


def index(request):
    categories = Category.objects.all()
    galleries = Gallery.objects.all()
    contacts = Contact.objects.all()
    abouts = About.objects.get()
    addresses = Address.objects.all()
    form = ContactForm()

    context = {
        "categories" : categories,
        "galleries" : galleries,
        "contacts" : contacts,
        "abouts" : abouts,
        "addresses" : addresses,
        "form" : form
    }

    return render(request,"index.html",context=context)