from django import forms
from .models import Fruit


class FruitCreationForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['name', 'image_url', 'description', 'nutrition']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.TextInput(attrs={'placeholder': 'Nutrition Info'}),
        }


class FruitEditForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['name', 'image_url', 'description', 'nutrition']
        labels = {
            'name': 'Name:',
            'image_url': 'Image URL:',
            'description': 'Description:',
            'nutrition': 'Nutrition:',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.TextInput(attrs={'placeholder': 'Nutrition Info'}),
        }


class FruitDeleteForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ['name', 'image_url', 'description']
        labels = {
            'name': 'Name:',
            'image_url': 'Image URL:',
            'description': 'Description:',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name', 'required': False, 'disabled': True}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Fruit Image URL', 'required': False, 'disabled': True}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Fruit Description', 'required': False, 'disabled': True}),
        }
