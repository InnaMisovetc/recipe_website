from django.db import models


class TimeStampMixin(models.Model):

    created_at = models.DateTimeField("Время создания рецета", auto_now_add=True)
    updated_at = models.DateTimeField("Время обновления рецета", auto_now=True)

    class Meta:
        abstract = True


class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class Recipe(TimeStampMixin):
    heading = models.CharField("Заголовок", max_length=50, unique=True)
    text = models.TextField("Рецепт")
    ingredients = models.ManyToManyField(Ingredient)
    image_url = models.URLField('Фотография')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.heading
