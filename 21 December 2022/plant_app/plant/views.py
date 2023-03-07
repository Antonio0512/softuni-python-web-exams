from django.shortcuts import render, redirect

from plant.forms import ProfileCreateForm, PlantCreateForm, PlantEditForm, PlantDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from plant.models import Profile, Plant


def home_page(request):
    profile = Profile.objects.all()

    context = {
        'profile': profile
    }
    return render(request, 'plant/home-page.html', context)


def catalogue_page(request):
    profile = Profile.objects.get()
    plants = Plant.objects.all()
    context = {
        'plants': plants,
        'profile': profile
    }
    return render(request, 'plant/catalogue.html', context)


def create_plant(request):
    profile = Profile.objects.get()
    form = PlantCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('page-catalogue')

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'plant/create-plant.html', context)


def details_plant(request, pk):
    profile = Profile.objects.get()
    plant = Plant.objects.get(pk=pk)

    context = {
        'profile': profile,
        'plant': plant
    }
    return render(request, 'plant/plant-details.html', context)


def edit_plant(request, pk):
    profile = Profile.objects.get()
    plant = Plant.objects.get(pk=pk)

    if request.method == 'POST':
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('page-catalogue')
    else:
        form = PlantEditForm(instance=plant)

        context = {
            'profile': profile,
            'form': form
        }
        return render(request, 'plant/edit-plant.html', context)


def delete_plant(request, pk):
    profile = Profile.objects.get()
    plant = Plant.objects.get(pk=pk)

    if request.method == 'POST':
        plant.delete()
        return redirect('page-catalogue')
    else:
        form = PlantDeleteForm(instance=plant)
        context = {
            'profile': profile,
            'form': form
        }
        return render(request, 'plant/delete-plant.html', context)


def create_profile(request):
    profile = Profile.objects.all()
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('page-catalogue')

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'plant/create-profile.html', context)


def details_profile(request):
    profile = Profile.objects.get()
    plants = Plant.objects.all()

    context = {
        'profile': profile,
        'plants': plants,
    }
    return render(request, 'plant/profile-details.html', context)


def edit_profile(request):
    profile = Profile.objects.get()

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')
    else:
        form = ProfileEditForm(instance=profile)
        context = {
            'form': form,
        }
        return render(request, 'plant/edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.get()
    plants = Plant.objects.all()

    if request.method == 'POST':
        plants.delete()
        profile.delete()
        return redirect('page-home')
    else:
        form = ProfileDeleteForm(instance=profile)
        context = {
            'form': form,
        }
        return render(request, 'plant/delete-profile.html', context)