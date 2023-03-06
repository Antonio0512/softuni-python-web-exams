from django.shortcuts import render, redirect

from music.forms import ProfileCreateForm, AlbumCreateForm, AlbumEditForm, AlbumDeleteForm, ProfileDeleteForm
from music.models import Profile, Album


def home_page(request):
    profile = Profile.objects.all()

    if profile:
        albums = Album.objects.all()
        context = {
            'albums': albums,
        }
        return render(request, 'music/home-with-profile.html', context)

    else:
        form = ProfileCreateForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('page-home')

        context = {
            'form': form,
            'hide_nav_links': True
        }

        return render(request, 'music/home-no-profile.html', context)


def add_album(request):
    form = AlbumCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('page-home')

    context = {
        'form': form,
    }
    return render(request, 'music/add-album.html', context)


def details_album(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album,
    }
    return render(request, 'music/album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'POST':
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('page-home')

    else:
        form = AlbumEditForm(instance=album)

        context = {
            'form': form,
        }
        return render(request, 'music/edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'POST':
        album.delete()
        return redirect('page-home')

    else:
        form = AlbumDeleteForm(instance=album)
        context = {
            'form': form,
        }
        return render(request, 'music/delete-album.html', context)


def details_profile(request):
    profile = Profile.objects.get()
    albums = Album.objects.all()
    context = {
        'profile': profile,
        'albums': albums
    }
    return render(request, 'music/profile-details.html', context)


def delete_profile(request):
    profile = Profile.objects.get()
    albums = Album.objects.all()

    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            albums.delete()
            profile.delete()
            return redirect('page-home')

    else:
        form = ProfileDeleteForm(instance=profile)
        context = {
            'form': form
        }
        return render(request, 'music/profile-delete.html', context)