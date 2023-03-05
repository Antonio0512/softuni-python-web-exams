from django.shortcuts import render, redirect

from notes.forms import FormCreateProfile, FormCreateNote, FormEditNote, FormDeleteNote
from notes.models import Profile, Note


def home_page(request):
    profiles = Profile.objects.all()

    if profiles:
        notes = Note.objects.all()

        context = {
            'notes': notes,
        }
        return render(request, 'notes/home-with-profile.html', context)

    else:
        form = FormCreateProfile(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect('page-home')

        context = {
            'form': form,
        }
        return render(request, 'notes/home-no-profile.html', context)


def create_note_page(request):
    form = FormCreateNote(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('page-home')

    context = {
        'form': form,
    }
    return render(request, 'notes/note-create.html', context)


def edit_note_page(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'POST':
        form = FormEditNote(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('page-home')

    form = FormEditNote(instance=note)
    context = {
        'form': form,
    }
    return render(request, 'notes/note-edit.html', context)


def delete_note_page(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'POST':
        note.delete()
        return redirect('page-home')

    form = FormDeleteNote(instance=note)
    context = {
        'form': form,
    }
    return render(request, 'notes/note-delete.html', context)


def details_note_page(request, pk):
    note = Note.objects.get(pk=pk)

    context = {
        'note': note,
    }
    return render(request, 'notes/note-details.html', context)


def profile_page(request):
    profile = Profile.objects.get()
    all_notes = Note.objects.all()
    context = {
        'all_notes': all_notes,
        'profile': profile
    }
    return render(request, 'notes/profile.html', context)


def profile_delete(request):
    profile = Profile.objects.get()
    all_notes = Note.objects.all()
    all_notes.delete()
    profile.delete()
    return redirect('page-home')