from django.contrib import admin

from web.models import About, Category, Contact, Gallery


admin.site.register(Category)


admin.site.register(Gallery)


class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "message"]

admin.site.register(Contact, ContactAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "image"]

admin.site.register(About, AboutAdmin)