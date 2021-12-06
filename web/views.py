import json
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings

from web.models import About, Address, Category, Contact, Gallery
from web.forms import ContactForm


def index(request):
    category_name = request.GET.get("category")

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
        "form" : form,
        "MEDIA_URL" : settings.MEDIA_URL,
    }

    return render(request,"index.html",context=context)


def contact(request):
    form = ContactForm(request.POST)

    if form.is_valid():
        if not Contact.objects.filter(email=request.POST.get('email')).exists():
            form.save()

            response_data = {
                "status" : "success",
                "title" : "Successfully Registered",
                "message" : "You are Subscribed to the News Letter"
            }
        else:
            response_data = {
                "status" : "error",
                "title" : "Already Registered",
                "message" : "You are Already Subscribed to the News Letter,no need to Subscribe again"
            }
    else:
        response_data = {
                "status" : "error",
                "title" : "Your Form is Not Valid",
                "message" : "Your Form is Not Valid,Try again"
            }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript")


def category(request):
    category_name = request.GET.get('category')

    print("###############################",category_name)
    if category_name:
        if category_name == "All":
            projects = Gallery.objects.all().values()
            data = list(projects)  
            response_data = {
                "title" : "success",
                "data" : data,
            }
        elif Category.objects.filter(name=category_name).exists():
            if Gallery.objects.filter(category__name=category_name).exists():
                projects = Gallery.objects.filter(category__name=category_name).values()
                data = list(projects)  

                response_data = {
                    "title" : "success",
                    "data" : data,
                }
            else:
                response_data = {
                    "title" : "failed",
                    "message" : "projects not found",
                }
        else:
            response_data = {
                "title" : "failed",
                "message" : "Category not found",
            }
    else:
        response_data = {
            "title" : "failed",
            "message" : "Category not found",
        }

    return JsonResponse({'response_data': response_data})


def gallery(request,pk):
    gallery = Gallery.objects.get(pk=pk)

    context = {
        "gallery" : gallery
    }

    return render(request,"gallery.html",context=context)