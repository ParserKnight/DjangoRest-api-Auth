
from django.urls import path
from rest_framework.authtoken import views
from .views import PeliculaList
from .views import PeliculaDetalle
from .views import PeliculaPost
from rest_framework.schemas import get_schema_view

urlpatterns = [
    
    path('', PeliculaList.as_view()),
    path('<str:titulo>/', PeliculaDetalle.as_view()),
    path('post', PeliculaPost.as_view()),

 ] 