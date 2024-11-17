from django.db import models

class Usuario(models.Model):
    dni = models.IntegerField(null=True)
    cuil = models.IntegerField(null=True)
