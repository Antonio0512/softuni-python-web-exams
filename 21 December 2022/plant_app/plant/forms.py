from django import forms

from plant.models import Profile, Plant


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []


class PlantCreateForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class PlantEditForm(PlantCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PlantDeleteForm(PlantCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'