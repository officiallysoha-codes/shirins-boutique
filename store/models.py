from django.db import models


# CATEGORY MODEL
class Category(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


# PRODUCT MODEL
class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)

    price = models.IntegerField()

    image = models.ImageField(upload_to='products/')


    def __str__(self):
        return self.name