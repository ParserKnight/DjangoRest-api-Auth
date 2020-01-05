from django.db import models

class Pelicula(models.Model):
	"""Modelo que definie a una pelicula"""
	
	titulo=models.CharField(max_length=50)
	descripcion = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	puntaje = models.IntegerField()
	
	def __str__(self):
		return self.titulo


