from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from books.forms import CategoryForm, BookForm
from books.models import Category, Book

__all__ = (
    'home', 'CategoryListView', 'CategoryDetailView', 'CategoryCreateView',
    'CategoryUpdateView', 'CategoryDeleteView', 'BookListView', 'BookDetailView',
    'BookCreateView', 'BookUpdateView', 'BookDeleteView',
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
    template_name = 'books/category_detail.html'

class CategoryCreateView(SuccessMessageMixin, CreateView):
    model = Category
    template_name = 'books/category_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('books:category')

    def get_success_message(self, cleaned_data):
        message = 'Категорія {name} успішно створена!'
        return message.format(**cleaned_data)


class CategoryUpdateView(SuccessMessageMixin, UpdateView):
    model = Category
    template_name = 'books/category_update.html'
    form_class = CategoryForm
    success_url = reverse_lazy('books:category')

    def get_success_message(self, cleaned_data):
        message = 'Категорія {name} успішно відредагована!'
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
        message = 'Категорія {name} успішно видалена!'
        return message.format(**cleaned_data)


class BookListView(ListView):
    model = Book
    template_name = 'books/books.html'
    paginate_by = 5
    ordering = ['name']

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(in_stock=True).prefetch_related('category')

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(in_stock=True)

class BookCreateView(SuccessMessageMixin, CreateView):
    model = Book
    template_name = 'books/book_create.html'
    form_class = BookForm
    success_url = reverse_lazy('books:book')

    def get_success_message(self, cleaned_data):
        message = 'Книгу {name} успішно створено'
        return message.format(**cleaned_data)

class BookUpdateView(SuccessMessageMixin, UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    form_class = BookForm
    success_url = reverse_lazy('books:book')

    def get_success_message(self, cleaned_data):
        message = 'Книга {name} успішно відредагована!'
        return message.format(**cleaned_data)

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('books:book')

    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message({'name': self.object.name})

        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        message = 'Книга {name} успішно видалена!'
        return message.format(**cleaned_data)