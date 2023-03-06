from django.shortcuts import render, redirect

from games.forms import ProfileCreateForm, CreateGameForm, EditGameForm, DeleteGameForm, ProfileEditForm, \
    ProfileDeleteForm
from games.models import Profile, Game


def home_page(request):
    profile = Profile.objects.all()
    context = {
        'profile': profile
    }
    return render(request, 'games/home-page.html', context)


def dashboard_page(request):
    games = Game.objects.all()
    context = {
        'games': games,
    }
    return render(request, 'games/dashboard.html', context)


def create_profile(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('page-home')

    context = {
        'form': form,
    }
    return render(request, 'games/create-profile.html', context)


def details_profile(request):
    profile = Profile.objects.get()
    all_games = Game.objects.all()
    avg_rating = average_rating(all_games)
    context = {
        'profile': profile,
        'games': all_games,
        'avg_rating': avg_rating
    }
    return render(request, 'games/details-profile.html', context)


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
        return render(request, 'games/edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.get()
    games = Game.objects.all()
    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            profile.delete()
            games.delete()
            return redirect('page-home')
    else:
        form = ProfileDeleteForm(instance=profile)
        context = {
            'form': form
        }
        return render(request, 'games/delete-profile.html', context)


def create_game(request):
    form = CreateGameForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('page-dashboard')

    context = {
        'form': form,
    }
    return render(request, 'games/create-game.html', context)


def details_game(request, pk):
    game = Game.objects.get(pk=pk)

    context = {
        'game': game
    }
    return render(request, 'games/details-game.html', context)


def edit_game(request, pk):
    game = Game.objects.get(pk=pk
                            )
    if request.method == 'POST':
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('page-dashboard')
    else:
        form = EditGameForm(instance=game)
        context = {
            'form': form
        }
        return render(request, 'games/edit-game.html', context)


def delete_game(request, pk):
    game = Game.objects.get(pk=pk)

    if request.method == 'POST':
        game.delete()
        return redirect('page-dashboard')
    else:
        form = DeleteGameForm(instance=game)
        context = {
            'form': form
        }
        return render(request, 'games/delete-game.html', context)


def average_rating(games):
    total_rating = 0
    if games:
        for game in games:
            total_rating += game.rating
        return total_rating / games.count()
    else:
        return 0