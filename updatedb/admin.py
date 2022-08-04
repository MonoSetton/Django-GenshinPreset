from django.contrib import admin
from .models import Character, Artifact_set, Sword, Claymore, Polearm, Catalyst, Bow

db_models = [Character, Artifact_set, Sword, Claymore, Polearm, Catalyst, Bow]
admin.site.register(db_models)