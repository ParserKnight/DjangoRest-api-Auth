
from rest_framework import serializers
from .models import Pelicula
from django.contrib.auth.models import User
from . import models


class PeliculaSerializer(serializers.ModelSerializer):

	class Meta:
		fields = ('id', 'titulo', 'descripcion', 'puntaje')
		model = models.Pelicula

