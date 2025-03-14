from django.db import models

# Create your models here.


class Calculator(models.Model):
    expression = models.CharField(max_length=100)
