from django.contrib import admin
from .models import Preset, Artifact

reg = [Preset, Artifact]

admin.site.register(reg)