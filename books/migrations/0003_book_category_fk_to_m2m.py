from django.db import migrations, models


def copy_fk_to_m2m(apps, schema_editor):
    Book = apps.get_model('books', 'Book')
    for book in Book.objects.all():
        book.categories_tmp.add(book.category_id)


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_category_options_remove_category_description_and_more'),
    ]

    operations = [

        migrations.AddField(
            model_name='book',
            name='categories_tmp',
            field=models.ManyToManyField(blank=True, related_name='+', to='books.category'),
        ),

        migrations.RunPython(copy_fk_to_m2m, migrations.RunPython.noop),

        migrations.RemoveField(
            model_name='book',
            name='category',
        ),

        migrations.RenameField(
            model_name='book',
            old_name='categories_tmp',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='books', to='books.category', verbose_name='Категорії'),
        ),
    ]
