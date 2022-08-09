from django.contrib import admin
from .models import Character, Artifact_set, Weapon

db_models = [Character, Artifact_set, Weapon]
admin.site.register(db_models)