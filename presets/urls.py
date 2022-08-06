from django.urls import path
from . import views

urlpatterns = [
    path('create_preset', views.create_preset, name='create_preset')
]