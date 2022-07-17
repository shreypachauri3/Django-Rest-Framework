from uuid import uuid4
import uuid
from django.db import models

# Create your models here.

class Author(models.Model):
    bookname=models.CharField(max_length=500)
    author=models.CharField(max_length=5000)

    def __str__(self) :
        return self.bookname

