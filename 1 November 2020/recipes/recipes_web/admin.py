from django.contrib import admin
from recipes_web.models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass
