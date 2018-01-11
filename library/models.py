from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=50, help_text='Book title')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=500, help_text='Book Description')

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return self.title+' --- '+self.author.name



class Author(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField(max_length=500)


    def get_absolute_url(self):
        return reverse('book-add')

    def __str__(self):
        return self.name
