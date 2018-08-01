from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from rest_framework import generics
from .models import Pelicula
from .serializers import PeliculaSerializer
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import AllowAny
from rest_framework.permissions import AllowAny, IsAuthenticated

class PeliculaList(generics.ListAPIView):
	"""
	Devuelve todas las peliculas de la base de datos
	"""
	queryset = Pelicula.objects.all()
	serializer_class=PeliculaSerializer

class PeliculaDetalle(generics.RetrieveAPIView):
	queryset = Pelicula.objects.all()
	serializer_class = PeliculaSerializer
	lookup_field = 'titulo'

class PeliculaPost(generics.CreateAPIView):
	permission_classes = (IsAuthenticated,)
	queryset = Pelicula.objects.all()
	serializer_class = PeliculaSerializer

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


