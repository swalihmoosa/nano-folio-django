from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery/")

    def __str__(self):
        return self.image

    class Meta:
        ordering = ["id"]


