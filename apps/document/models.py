from django.db import models
from django.shortcuts import reverse

from apps.employee.models import Employee


class Document(models.Model):
    description = models.CharField(max_length=100)
    created_by = models.ForeignKey(Employee, on_delete=models.PROTECT)
    archive = models.FileField(upload_to='document')

    def get_absolute_url(self):
        return reverse('update_employee', args=[self.created_by.id])

    def __str__(self):
        return self.description
