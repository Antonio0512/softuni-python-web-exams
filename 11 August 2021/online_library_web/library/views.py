from django.shortcuts import render, redirect

from library.forms import ProfileAddForm, BookAddForm, EditBookForm, ProfileEditForm, ProfileDeleteForm
from library.models import Profile, Book


def home_page(request):
    profile = Profile.objects.all()

    if profile:
        books = Book.objects.all()

        context = {
            'books': books
        }
        return render(request, 'library/home-with-profile.html', context)

    else:
        form = ProfileAddForm(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect('page-home')

        context = {
            'form': form,
        }

        return render(request, 'library/home-no-profile.html', context)


def book_add_page(request):
    form = BookAddForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('page-home')

    context = {
        'form': form,
    }
    return render(request, 'library/add-book.html', context)


def book_edit_page(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('page-home')
    else:
        form = EditBookForm(instance=book)

        context = {
            'form': form,
        }
        return render(request, 'library/edit-book.html', context)


def book_delete_page(request, pk):
    book = Book.objects.get(pk=pk)

    book.delete()
    return redirect('page-home')


def book_details_page(request, pk):
    book = Book.objects.get(pk=pk)

    context = {
        'book': book
    }
    return render(request, 'library/book-details.html', context)


def profile_page(request):
    profile = Profile.objects.get()

    context = {
        'profile': profile,
    }

    return render(request, 'library/profile.html', context)


def profile_edit_page(request):
    profile = Profile.objects.get()

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('page-profile')
    else:
        form = ProfileEditForm(instance=profile)
        context = {
            'form': form
        }
        return render(request, 'library/edit-profile.html', context)


def profile_delete_page(request):
    profile = Profile.objects.get()
    books = Book.objects.all()

    if request.method == 'POST':
        books.delete()
        profile.delete()
        return redirect('page-home')

    else:
        form = ProfileDeleteForm(instance=profile)
        context = {
            'form': form,
        }
        return render(request, 'library/delete-profile.html', context)
