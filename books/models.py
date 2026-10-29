from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Категорія")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['name']


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва книги")
    author = models.CharField(max_length=100, verbose_name="Автор")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Ціна")
    description = models.TextField(verbose_name="Опис")
    stock = models.PositiveIntegerField(default=0, verbose_name="Кількість на складі")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title']