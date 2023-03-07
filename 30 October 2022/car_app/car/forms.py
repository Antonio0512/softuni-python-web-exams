from django import forms

from car.models import Profile, Car


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']

        widgets = {
            'password': forms.PasswordInput()
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CarEditForm(CarCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CarDeleteForm(CarCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'