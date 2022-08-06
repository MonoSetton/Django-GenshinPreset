from django.forms import ModelForm
from .models import Preset

class PresetForm(ModelForm):
    class Meta:
        model = Preset
        fields = '__all__'

        