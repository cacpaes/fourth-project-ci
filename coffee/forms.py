from .models import CoffeePost
from django import forms


class CoffeePostForm(forms.ModelForm):
    """
    Form class to create coffee post.
    """
    coffee_brand = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ex: Nespresso, ...', 'class': 'form-control'}), label="Brand")
    coffee_origin = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ex: Minas Gerais, ...', 'class': 'form-control'}), label="Origin")
    coffee_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ex: Colombiano, ...', 'class': 'form-control'}), label="Name")
    coffee_content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Ex: Content Coffee, ...', 'class': 'form-control'}), label="Content")
    coffee_image = forms.FileField(widget=forms.FileInput(attrs={'accept':'image/*'}))



    class Meta:
        model = CoffeePost
        fields = [
            'coffee_brand',
            'coffee_origin',
            'coffee_name',
            'coffee_content',
            'coffee_image'
        ]