from django.shortcuts import render, redirect
from .forms import PresetForm


def create_preset(request):
    form = PresetForm()
    if request.method == 'POST':
        form = PresetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'presets\create_preset.html', {'form': form})
