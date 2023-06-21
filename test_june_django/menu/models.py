from django.db import models

# Create your models here.

class Menu(models.Model):

    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title} {self.price}'

class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Dish(models.Model):

    dishes = models.ForeignKey(Menu, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.dishes}:{self.category}'