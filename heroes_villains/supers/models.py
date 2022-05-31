from django.db import models
from django.forms import CharField

# Create your models here.


class Power(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"


class Super(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    powers = models.ManyToManyField(Power)
    catchphrase = models.CharField(max_length=255)
    super_type = models.ForeignKey(
        "super_types.SuperType", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} - {self.super_type}"
