from django.db import models
from django.urls import reverse
from apps.employee.models import Employee


class Overtime(models.Model):
    remark = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    hour = models.DecimalField(max_digits=5, decimal_places=2)

    def get_absolute_url(self):
        return reverse('update_overtime', args=[self.id])

    def __str__(self):
        return self.remark
