from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, help_text='Name company')

    def __str__(self):
        return self.name
