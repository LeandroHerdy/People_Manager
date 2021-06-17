from django.db import models
from django.urls import reverse


def get_absolute_url():
    return reverse('home')


class Company(models.Model):
    name = models.CharField(max_length=100, help_text='Name company')

    def __str__(self):
        return self.name

