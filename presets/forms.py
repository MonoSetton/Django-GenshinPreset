from django.forms import ModelForm, inlineformset_factory
from .models import Preset


class PresetForm(ModelForm):
    class Meta:
        model = Preset
        fields = '__all__'

        