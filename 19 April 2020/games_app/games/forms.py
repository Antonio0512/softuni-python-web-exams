from django import forms
from games.models import Profile, Game


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = 'email', 'age', 'password'

        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class EditGameForm(CreateGameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DeleteGameForm(CreateGameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
