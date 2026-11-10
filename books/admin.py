from django.contrib import admin

from books.models import Category, Book

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )

    list_editable = ('name', )

admin.site.register(Category, CategoryAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'in_stock', 'get_category')
    list_filter = ('category',)
    filter_horizontal = ('category',)

    def get_category(self, obj):
        return ', '.join(c.name for c in obj.category.all())

    get_category.short_description = 'Категорії'

admin.site.register(Book, BookAdmin)