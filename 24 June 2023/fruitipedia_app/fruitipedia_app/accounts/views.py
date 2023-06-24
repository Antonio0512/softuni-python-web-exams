from django.shortcuts import render, redirect
from . import forms
from . import models
from ..fruitipedia.models import Fruit


def create_profile(request):
    form = forms.ProfileCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('page-home')

    context = {
        'form': form
    }
    return render(request, 'fruitipedia/create-profile.html', context)


def details_profile(request):
    profile = models.UserProfile.objects.get()
    fruits = Fruit.objects.count()
    context = {
        'profile': profile,
        'fruits': fruits
    }
    return render(request, 'fruitipedia/details-profile.html', context)


def edit_profile(request):
    profile = models.UserProfile.objects.get()
    if request.method == 'POST':
        form = forms.ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')

    else:
        form = forms.ProfileEditForm(instance=profile)
        context = {
            'profile': profile,
            'form': form
        }
        return render(request, 'fruitipedia/edit-profile.html', context)


def delete_profile(request):
    profile = models.UserProfile.objects.get()
    fruits = Fruit.objects.all()
    if request.method == 'POST':
        profile.delete()
        fruits.delete()
        return redirect('page-home')
    else:
        context = {
            'profile': profile,
        }
        return render(request, 'fruitipedia/delete-profile.html', context)
