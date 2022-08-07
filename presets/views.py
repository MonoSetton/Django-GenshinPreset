from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import *

def update_art(request, pk):
    PresetFormSet = inlineformset_factory(Preset, Artifact, fields=('stat', 'status',), extra=4, can_delete=False, max_num=5)
    preset = Preset.objects.get(id=pk)
    formset = PresetFormSet(instance=preset)

    if request.method == 'POST':
        formset = PresetFormSet(request.POST, instance=preset)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    return render(request, 'presets\create_preset.html', {'formset': formset})


def details(request, pk):
    artifacts = Artifact.objects.all()
    return render(request, 'presets\details.html', {'artifacts': artifacts})