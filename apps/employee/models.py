from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.urls import reverse

from apps.company.models import Company
from apps.departament.models import Departament


class Employee(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departament = models.ManyToManyField(Departament)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    #image = models.ImageField()

    def get_absolute_url(self):
        return reverse('list_employee')

    @property
    def total_hour(self):
        total = self.overtime_set.all().aggregate(Sum('hour'))['hour__sum']
        return total

    def __str__(self):
        return self.name
