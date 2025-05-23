# Generated by Django 5.2 on 2025-04-16 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_book_values_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='book_values',
            name='description',
        ),
        migrations.CreateModel(
            name='bookdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
                ('pages', models.PositiveIntegerField(null=True)),
                ('description', models.TextField()),
                ('book', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='book.book_values')),
            ],
        ),
    ]
