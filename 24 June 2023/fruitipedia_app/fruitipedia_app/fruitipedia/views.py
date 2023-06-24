from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from . import models
from . import forms
from ..accounts.models import UserProfile


# Create your views here.
def homepage(request):
    profile = UserProfile.objects.all()
    context = {
        'profile': profile
    }
    return render(request, 'fruitipedia/index.html', context)


def dashboard(request):
    profile = UserProfile.objects.all()
    fruits = models.Fruit.objects.all()
    context = {
        'profile': profile,
        'fruits': fruits
    }
    return render(request, 'fruitipedia/dashboard.html', context)


def create_fruit(request):
    profile = UserProfile.objects.all()
    form = forms.FruitCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('page-dashboard')
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'fruitipedia/create-fruit.html', context)


def details_fruit(request, pk):
    profile = UserProfile.objects.all()
    fruit = models.Fruit.objects.get(pk=pk)

    context = {
        'profile': profile,
        'fruit': fruit
    }
    return render(request, 'fruitipedia/details-fruit.html', context)


def edit_fruit(request, pk):
    profile = UserProfile.objects.all()
    fruit = models.Fruit.objects.get(pk=pk)

    if request.method == 'POST':
        form = forms.FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('page-dashboard')
        else:
            context = {
                'profile': profile,
                'form': form
            }
            return render(request, 'fruitipedia/edit-fruit.html', context)
    else:
        form = forms.FruitEditForm(instance=fruit)
        context = {
            'profile': profile,
            'form': form
        }
        return render(request, 'fruitipedia/edit-fruit.html', context)


def delete_fruit(request, pk):
    profile = UserProfile.objects.all()
    fruit = models.Fruit.objects.get(pk=pk)

    if request.method == 'POST':
        fruit.delete()
        return redirect('page-dashboard')
    else:
        form = forms.FruitDeleteForm(instance=fruit)
        context = {
            'profile': profile,
            'form': form
        }
        return render(request, 'fruitipedia/delete-fruit.html', context)
