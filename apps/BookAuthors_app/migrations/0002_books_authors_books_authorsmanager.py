# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 19:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookAuthors_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='books_authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookAuthors_app.authors')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookAuthors_app.books')),
            ],
        ),
        migrations.CreateModel(
            name='Books_AuthorsManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
