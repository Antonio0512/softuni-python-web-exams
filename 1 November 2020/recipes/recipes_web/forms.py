from django import forms
from recipes_web.models import Recipe


class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeEditForm(RecipeCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class RecipeDeleteForm(RecipeCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
