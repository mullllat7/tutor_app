from django.db import models

from application.category.models import Category


class Subcategory(models.Model):
    name_of_subcat = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False, related_name='subcategory')
    description = models.TextField()
    images = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return self.name_of_subcat


class SubcategoryImage(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='subcategory_image')
    image = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return self.subcategory.name_of_subcat

