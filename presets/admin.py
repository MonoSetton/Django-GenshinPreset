from django.contrib import admin
from .models import Preset, Artifact

reg = [Preset, Artifact]

class ArtAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(reg, ArtAdmin)
