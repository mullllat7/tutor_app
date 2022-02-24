from django.shortcuts import render
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from application.theme.models import Theme
from application.theme.serializers import ThemeSerializers, ThemeDetailSerializer


class ThemeListView(generics.ListAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializers
    pagination_class = PageNumberPagination

    def get_serializer_context(self):
        return {'request':self.request}


class ThemeDetailView(generics.RetrieveAPIView):

    queryset = Theme.objects.all()
    serializer_class = ThemeDetailSerializer
