from django.forms import ModelForm, fields, widgets
from web.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "name" : widgets.TextInput(attrs={
                "placeholder" : "Name"
            }),
            "email" : widgets.EmailInput(attrs={
                "placeholder" : "Email"
            }),
            "message" : widgets.Textarea(attrs={
                "placeholder" : "Message",
                "rows" : 5,
                "cols" : 30
            })
        }