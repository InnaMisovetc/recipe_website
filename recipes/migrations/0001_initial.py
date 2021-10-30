# Generated by Django 3.2.8 on 2021-10-30 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания рецета')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления рецета')),
                ('heading', models.CharField(max_length=50, unique=True, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Рецепт')),
                ('image_url', models.URLField(verbose_name='Фотография')),
                ('ingredients', models.ManyToManyField(to='recipes.Ingredient')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
    ]