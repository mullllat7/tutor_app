from django.shortcuts import render
from rest_framework import generics

from application.category.models import Category
from application.category.serializers import CategorySerializers


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
