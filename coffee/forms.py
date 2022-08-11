from .models import CoffeePost
from django import forms


class CoffeePostForm(forms.ModelForm):
    """
    Form class to create coffee post.
    """
    brand = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ex: Nespresso, ...'}))
    origin = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ex: Minas Gerais, ...'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ex: Colombiano, ...'}))

    class Meta:
        model = CoffeePost
        fields = [
            'coffee_brand',
            'origin',
            'name',
        ]