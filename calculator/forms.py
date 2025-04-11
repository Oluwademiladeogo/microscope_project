from django import forms
from .models import Specimen

class SpecimenForm(forms.ModelForm):
    class Meta:
        model = Specimen
        fields = ['username', 'specimen_name', 'microscope_size', 'magnification']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'specimen_name': forms.TextInput(attrs={'class': 'form-control'}),
            'microscope_size': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'magnification': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
        }
