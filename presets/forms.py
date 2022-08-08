from django.forms import ModelForm
from .models import Preset, Artifact


class PresetForm(ModelForm):
    class Meta:
        model = Preset
        fields = ['name']




        