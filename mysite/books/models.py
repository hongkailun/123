from django.db import models

# Create your models here.
class Author(models.Model):
    AuthorID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=200)
    Age = models.IntegerField(max_length=50)
    Country = models.CharField(max_length=100)

class Book(models.Model):
    ISBN = models.CharField(primary_key=True,max_length=100)
    Title = models.CharField(max_length=200)
    AuthorID = models.IntegerField(max_length=100)
    Publisher = models.CharField(max_length=200)
    PublishDate = models.CharField(max_length=200)
    Price = models.FloatField(max_length=200)
