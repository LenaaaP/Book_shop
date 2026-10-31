from django.contrib import admin

from books.models import Category, Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'in_stock', 'category')

    list_editable = ('price', 'name', 'in_stock')

admin.site.register(Book, BookAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    list_editable = ('name', )

admin.site.register(Category, CategoryAdmin)