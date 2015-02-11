from django.db import models

class Usuario(models.Model):
	nombre = models.CharField(max_length=200)
	password = models.CharField(max_length=256)
	id_usuario = models.CharField(max_length=30)
	correo = models.CharField(max_length=100)
