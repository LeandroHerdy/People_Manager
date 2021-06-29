from django.db import models
from django.urls import reverse
from apps.company.models import Company


class Departament(models.Model):
    name = models.CharField(max_length=70)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('list_departament')

    def __str__(self):
        return self.name
