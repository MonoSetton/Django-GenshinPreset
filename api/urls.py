from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview),
    path('character-list/', views.character_list),
    path('weapon-list/', views.weapon_list),
    path('artifact-set-list/', views.artifact_set_list),

]