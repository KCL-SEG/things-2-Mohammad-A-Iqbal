"""Forms of the project."""
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your forms here.
class ThingForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=50)
    description = forms.CharField(label='Description:', max_length=120,
                                widget=forms.Textarea())
    quantity = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)],
                                widget=forms.NumberInput()) 

    def clean(self):
        super().clean()
