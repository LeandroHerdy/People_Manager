from django.db import models


class Overtime(models.Model):
    justification = models.CharField(max_length=100)

    def __str__(self):
        return self.justification
