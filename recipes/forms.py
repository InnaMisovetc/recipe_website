from django import forms

from .models import Recipe


class CreateForm(forms.ModelForm):
    additional_ingredients = forms.CharField(label='Новые ингредиенты (через пробел)',
                                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    field_order = ['heading', 'ingredients', 'additional_ingredients', 'text', 'image_url']

    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {'heading': forms.TextInput(attrs={'class': 'form-control'}),
                   'ingredients': forms.SelectMultiple(attrs={'class': 'form-control'}),
                   'text': forms.Textarea(attrs={'class': 'form-control'}),
                   'image_url': forms.TextInput(attrs={'class': 'form-control'})}
        labels = {'ingredients': 'Ингредиенты', 'image_url': 'Ссылка на фотографию'}
