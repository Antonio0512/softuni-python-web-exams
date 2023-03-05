from django import forms
from notes.models import Profile, Note


class FormCreateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class FormCreateNote(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class FormEditNote(FormCreateNote):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class FormDeleteNote(FormCreateNote):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'