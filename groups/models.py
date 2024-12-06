from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Group(models.Model):
    group = models.CharField(max_length=100)
    group_type = models.CharField(max_length=100)

