from django.shortcuts import render, redirect
from authentication.forms import SignForm, LoginForm, ModificationForm
from authentication.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST


# Create your views here.
def home(request):
     form = LoginForm(request.POST or None)
     if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Connexion réussie")
                return redirect('profil')
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
     return render(request, 'authentication/index.html', context={'form': form})

def create(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Compte créé avec succès! Vous pouvez maintenant vous connecter.")
            return redirect('home')
    else:
        form = SignForm()
    return render(request, 'authentication/create.html', {'form': form})


@login_required
def profil(request):
    return render(request, 'authentication/profil.html')


@require_POST
def logout_user(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('home')

@login_required
def modif(request):
    form = ModificationForm(instance=request.user)
    if request.method == 'POST':
        form = ModificationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profil mis à jour avec succès")
            return redirect('profil')
    return render(request, 'authentication/modif.html', context={'form':form})