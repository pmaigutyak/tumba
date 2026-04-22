from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tumb(models.Model):
    category = models.ForeignKey(Category, models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='tumbs/')

    def __str__(self):
        return self.title