import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Категорія', 'verbose_name_plural': 'Категорії'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Назва книги')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Ціна')),
                ('description', models.TextField(verbose_name='Опис')),
                ('in_stock', models.BooleanField(default=True, verbose_name='Наявність на складі')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.category', verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
