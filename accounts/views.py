from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from presets.models import Preset


@login_required(login_url='/login')
def home(request):
    presets = Preset.objects.filter(author=request.user)
    characters = set()
    for preset in presets:
        characters.add(preset.character)
    return render(request, 'accounts/home.html', {'presets': presets, 'characters': characters})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'registration/signup.html', {'form': form})

