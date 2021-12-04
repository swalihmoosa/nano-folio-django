from django.contrib import admin

from web.models import Category, Contact, Gallery


admin.site.register(Category)


admin.site.register(Gallery)


class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "message"]

admin.site.register(Contact,ContactAdmin)