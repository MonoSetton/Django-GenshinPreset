from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .forms import PresetForm, PresetUpdateForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.exceptions import BadRequest


@login_required(login_url='/login')
def update_art(request, pk):
    PresetFormSet = inlineformset_factory(Preset, Artifact, fields=('set', 'main', 'first', 'second', 'third', 'fourth',
                                                                    'status',), extra=5, can_delete=False, max_num=5)
    preset = Preset.objects.get(id=pk)
    formset = PresetFormSet(instance=preset)
    if preset.author == request.user:
        if request.method == 'POST':
            formset = PresetFormSet(request.POST, instance=preset)
            if formset.is_valid():
                formset.save()
                return redirect('/details/'+pk)
        return render(request, 'presets/update_art.html', {'formset': formset})
    else:
        raise BadRequest("You do not have permission to see this site")


@login_required(login_url='/login')
def details(request, pk):
    preset = Preset.objects.get(id=pk)
    artifacts = Artifact.objects.filter(preset=preset)
    if preset.author == request.user:
        return render(request, 'presets/details.html', {'artifacts': artifacts, 'preset': preset})
    else:
        raise BadRequest("You do not have permission to see this site")


@login_required(login_url='/login')
def create_preset(request):
    if request.method == 'POST':
        form = PresetForm(request.POST)
        if form.is_valid():
            preset = form.save(commit=False)
            preset.author = request.user
            form.save()
            return redirect('details/' + str(preset.id))
    else:
        form = PresetForm()
    return render(request, 'presets/create_preset.html', {'form': form})


@login_required(login_url='/login')
def delete_preset(request, pk):
    preset = Preset.objects.get(id=pk)
    if preset.author == request.user:
        if request.method == 'POST':
            preset.delete()
            return redirect('/')
        return render(request, 'presets/delete.html', {'preset': preset})
    else:
        raise BadRequest("You do not have permission to see this site")


@login_required(login_url='/login')
def update_preset(request, pk):
    preset = Preset.objects.get(id=pk)
    form = PresetUpdateForm(instance=preset)
    if request.method == 'POST':
        form = PresetUpdateForm(request.POST, instance=preset)
        if form.is_valid():
            form.save()
            return redirect('/details/'+pk)
    return render(request, 'presets/update_preset.html', {'form': form})
