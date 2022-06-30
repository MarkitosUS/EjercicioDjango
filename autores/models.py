from email.mime import image
from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=200)
    image = ImageField(upload_to='autores/images/')
    url = URLField(blank=True)