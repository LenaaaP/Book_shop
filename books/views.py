from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from books.forms import CategoryForm
from books.models import Category

__all__ = (
    'home', 'CategoryListView', 'CategoryDetailView', 'CategoryCreateView', 'CategoryUpdateView', 'CategoryDeleteView'
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

class CategoryCreateView(SuccessMessageMixin, CreateView):
    model = Category
    template_name = 'books/category_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('books:category')

    def get_success_message(self, cleaned_data):
        message = 'Категорія {name} успішно створенa!'
        return message.format(**cleaned_data)


class CategoryUpdateView(SuccessMessageMixin, UpdateView):
    model = Category
    template_name = 'books/category_update.html'
    form_class = CategoryForm
    success_url = reverse_lazy('books:category')

    def get_success_message(self, cleaned_data):
        message = 'Категорія {name} успішно відредагованa!'
        return message.format(**cleaned_data)

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'books/category_delete.html'
    success_url = reverse_lazy('books:category')

    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message({'name': self.object.name})

        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        message = 'Категорія {name} успішно видалена'
        return message.format(**cleaned_data)