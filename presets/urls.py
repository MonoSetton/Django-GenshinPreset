from django.urls import path
from . import views


urlpatterns = [
    path('update_art/<str:pk>', views.update_art, name='update_art'),
    path('details/<str:pk>', views.details, name='details'),
]