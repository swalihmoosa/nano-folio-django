from django.urls import path
from web.views import category, index, contact, gallery


app_name = "web"

urlpatterns = [
    path("",index,name="index"),
    path("contact",contact,name="contact"),
    path("category/",category, name="category"),
    path("gallery/<pk>",gallery, name="gallery")
]