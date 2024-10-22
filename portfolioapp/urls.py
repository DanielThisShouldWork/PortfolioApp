

from django.urls import path
from . import views  # Importa le viste dalla tua app

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contacts/', views.contacts, name='contacts'),
]