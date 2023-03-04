from django.shortcuts import render, redirect

from recipes_web.forms import RecipeCreateForm, RecipeEditForm, RecipeDeleteForm
from recipes_web.models import Recipe


def home_page(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes
    }

    return render(request, 'recipes_web/index.html', context)


def create_page(request):
    form = RecipeCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('page-home')

    else:
        context = {
            'form': form,
        }
        return render(request, 'recipes_web/create.html', context)


def edit_page(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'POST':
        form = RecipeEditForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('page-home')
    else:
        form = RecipeEditForm(instance=recipe)

        context = {
            'form': form
        }
        return render(request, 'recipes_web/edit.html', context)


def delete_page(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'POST':
        recipe.delete()
        return redirect('page-home')

    else:
        form = RecipeDeleteForm(instance=recipe)

        contex = {
            'form': form
        }
        return render(request, 'recipes_web/delete.html', contex)


def details_page(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    context = {
        'recipe': recipe,
        'ingredients': recipe.ingredients.split(', ')
    }

    return render(request, 'recipes_web/details.html', context)
