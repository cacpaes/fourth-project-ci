from .models import CoffeePost, Comment
from django import forms


class CoffeePostForm(forms.ModelForm):
    """
    Form class to create coffee post.
    """
    coffee_brand = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ex: Nespresso, ...', 'class': 'form-control'}), label="Brand",
        max_length=30)
    coffee_origin = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ex: Minas Gerais, ...', 'class': 'form-control'}), label="Origin",
        max_length=30)
    coffee_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ex: Colombiano, ...', 'class': 'form-control'}), label="Name",
        max_length=30)
    coffee_content = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Ex: Content Coffee, ...', 'class': 'form-control'}),
        label="Content", max_length=300)
    coffee_image = forms.FileField(widget=forms.FileInput(attrs={'accept': 'image/*'}))

    class Meta:
        model = CoffeePost
        fields = [
            'coffee_brand',
            'coffee_origin',
            'coffee_name',
            'coffee_content',
            'coffee_image'
        ]


class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Name", max_length=80)
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Email")
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label="Comment")

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
