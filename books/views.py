from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from books.forms import CategoryForm
from books.models import Category

__all__ = (
    'home', 'CategoryListView', 'CategoryDetailView', 'CategoryCreateView'
)


def home(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()

    form = CategoryForm()
    qs = Category.objects.all()
    context = {'object_list': qs, 'form': form}
    return render(request, 'books/categories.html', context)

class CategoryListView(ListView):
    model = Category
    template_name = 'books/categories.html'

class CategoryDetailView(DetailView):
    model = Category
    # template_name = 'books/category_detail.html'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'books/category_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('books:category')