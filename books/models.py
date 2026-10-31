from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Категорія")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['name']


class Book(models.Model):
    name = models.CharField(max_length=200, verbose_name='Назва книги')
    author = models.CharField(max_length=100, verbose_name='Автор')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Ціна')
    description = models.TextField(verbose_name='Опис')
    in_stock = models.BooleanField(
        default=True, verbose_name='Наявність на складі',
    )
    category = models.ForeignKey(
        'books.Category',
        on_delete=models.PROTECT,
        related_name='books',
        verbose_name='Категорія',
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name