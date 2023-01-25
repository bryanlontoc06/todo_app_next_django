from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Author(models.Model):
    authorName = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.authorName


class Todo(models.Model):
    description = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('Image', overwrite=True,format="jpg")

    def __str__(self):
        return self.description