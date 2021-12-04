from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery/")
    Category = models.ForeignKey("web.Category",on_delete=models.CASCADE)

    def __str__(self):
        return self.image

    class Meta:
        ordering = ["id"]


class Contact(models.Model):
    name = models.CharField(max_length=155)
    email = models.EmailField(max_length=155)
    message = models.TextField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]