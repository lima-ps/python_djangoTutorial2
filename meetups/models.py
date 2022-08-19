from ctypes import addressof
from distutils.command.upload import upload
import email
from pydoc import describe
from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    
    def __str__(self): #isso garante que o objeto possa ser chamado como String
        return f'{self.name} ({self.address})'

class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participant = models.ManyToManyField(Participant, blank=True, null=True) #relacoes manytomany precisam ser referenciadas apenas em um modelo.

    def __str__(self):
        return f'{self.title} - {self.slug}'