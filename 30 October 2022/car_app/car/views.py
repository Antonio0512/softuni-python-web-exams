from django.shortcuts import render, redirect

from car.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm, ProfileDeleteForm
from car.models import Profile, Car


def home_page(request):
    profile = Profile.objects.all()

    context = {
        'profile': profile
    }
    return render(request, 'car/index.html', context)


def catalogue_page(request):
    cars = Car.objects.all()

    context = {
        'cars': cars
    }
    return render(request, 'car/catalogue.html', context)


def create_profile(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('page-catalogue')

    context = {
        'form': form
    }
    return render(request, 'car/profile-create.html', context)


def details_profile(request):
    profile = Profile.objects.get()
    cars_sum = _calculate_cat_sum(Car.objects.all())
    context = {
        'profile': profile,
        'cars_sum': cars_sum
    }
    return render(request, 'car/profile-details.html', context)


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
            'form': form
        }
        return render(request, 'car/profile-edit.html', context)


def delete_profile(request):
    profile = Profile.objects.get()
    cars = Car.objects.all()

    if request.method == 'POST':
        cars.delete()
        profile.delete()
        return redirect('page-home')
    else:
        form = ProfileDeleteForm(instance=profile)
        context = {
            'form': form
        }
        return render(request, 'car/profile-delete.html', context)


def create_car(request):
    form = CarCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('page-catalogue')

    context = {
        'form': form
    }
    return render(request, 'car/car-create.html', context)


def details_car(request, pk):
    car = Car.objects.get(pk=pk)
    context = {
        'car': car
    }
    return render(request, 'car/car-details.html', context)


def edit_car(request, pk):
    car = Car.objects.get(pk=pk)

    if request.method == 'POST':
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('page-catalogue')
    else:
        form = CarEditForm(instance=car)
        context = {
            'form': form
        }
        return render(request, 'car/car-edit.html', context)


def delete_car(request, pk):
    car = Car.objects.get(pk=pk)

    if request.method == 'POST':
        car.delete()
        return redirect('page-catalogue')
    else:
        form = CarDeleteForm(instance=car)
        context = {
            'form': form
        }
        return render(request, 'car/car-delete.html', context)


def _calculate_cat_sum(cars):
    total_sum = 0
    if cars:
        for car in cars:
            total_sum += car.price
        return total_sum
    return 0
