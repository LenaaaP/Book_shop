from django import forms

from books.models import Category, Book


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


class BookForm(forms.ModelForm):
    name = forms.CharField(
        label="Книги", max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть назву'
        })
    )
    description = forms.CharField(
        label="Опис книги", max_length=None,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть опис'
        })
    )
    price = forms.DecimalField(
        label="Ціна", widget=forms.NumberInput(
            attrs={'class': 'form-control', })
    )
    category = forms.ModelMultipleChoiceField(
        label='Категорії', queryset=Category.objects.all(), required=False,
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control js-select2'
        })
    )

    class Meta:
        model = Book
        fields = '__all__'
