from django.db import models

class Tumb(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='tumbs/')
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title