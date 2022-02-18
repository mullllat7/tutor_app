from django.db import models

from application.category.utils import slug_generator


class Category(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, primary_key=True, unique=True, blank=True)

    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slug_generator(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.title}'
        return self.title


class CategoryImage(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_image')
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.category.title

