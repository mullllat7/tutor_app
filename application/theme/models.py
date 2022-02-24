from django.db import models

from application.subcategory.models import Subcategory


class Theme(models.Model):

    theme = models.CharField(max_length=255)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='theme')
    topic_of_theme = models.TextField()
    example = models.TextField(max_length=255, null=True, blank=True)
    image_of_example = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return self.theme


class ThemeImage(models.Model):

    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='theme_image')
    image = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return self.theme.theme

