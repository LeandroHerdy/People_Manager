from django.contrib.auth.models import User
from django.db import models

from apps.company.models import Company
from apps.departament.models import Departament


class Employee(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departament = models.ManyToManyField(Departament)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
