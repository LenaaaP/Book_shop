from django import forms

from books.models import Category


class HtmlForm(forms.Form):
    name = forms.CharField(label="Категорія", max_length=100)

class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        label="Категорія",
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть назву'
        })
    )

    class Meta:
        model = Category
        fields = ('name',)